"""Model state viewer

Based on artist.py in TST-MD
"""
import logging
from pathlib import Path
from typing import List, Optional

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.contour import QuadContourSet
from matplotlib.image import AxesImage
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt

from tissue_simulation_toolkit.ecm.ecm import ParticleType


_logger = logging.getLogger(__name__)


class StatePlotter:
    """Plots the simulation state on the screen or to a file."""
    def __init__(self, sizex: int, sizey: int, img_height: int = 480) -> None:
        """Create a Viewer

        Image width will be set automatically based on the height and the sizex/sizey
        aspect ratio.

        Args:
            sizex: Length in the x direction of the model domain
            sizey: Length in the y direction of the model domain
            img_height: Height of the image in pixels
        """
        self._sizex = sizex
        self._sizey = sizey
        self._img_height = img_height
        self._img_width = int(img_height * sizex / sizey)
        self._dpi = 100.0
        offset = 75.0

        figsize = (self._img_width / self._dpi, self._img_height / self._dpi)
        self._fig = plt.figure(figsize=figsize, dpi=self._dpi)
        self._ax = plt.axes((0, 0, 1, 1), frameon = False, xticks=[], yticks=[])
        
        self._ax.set_xlim(-offset, self._sizex + offset)
        # flip y-axis to match TST graphics
        self._ax.set_ylim(self._sizey + offset, -offset)

        x = np.linspace(0.0, self._sizex, self._sizex)
        y = np.linspace(0.0, self._sizey, self._sizey)
        self._cpm_grid = np.meshgrid(x, y, indexing='ij')

        self._bond_lines: List[Line2D] = []
        self._adhesion_marks, = plt.plot(
                [], [], 'o', alpha = 1.0, markersize = 2,
                zorder = 2.1)
        self._cpm_contours: Optional[QuadContourSet] = None
        self._cpm_contour_fill: Optional[QuadContourSet] = None
        self._pde_image: Optional[AxesImage] = None
        self._act_image: Optional[AxesImage] = None

        plt.ioff()

    def draw(
            self, i: int, par_pos: npt.NDArray[np.float64],
            par_type: npt.NDArray[np.int32], bond_groups: npt.NDArray[np.int32],
            pde: npt.NDArray[np.float64], 
            cpm: npt.NDArray[np.int32], actfield: dict, 
            draw: bool = True, save: bool = True, out_dir: Optional[Path] = None,
            output_format: str = 'png') -> None:
        """Update the diagram with new data

        Args:
            par_pos: Particle positions as an Nx2 array
            par_type: Particle types as an N-vector
            bond_groups: Ids of bonded particles, Mx2 array
            pde: Concentrations, L x SizeX x SizeY array
            cpm: Cellular Potts state, SizeX x SizeY array
            actfield: Act level, SizeX x SizeY array
            draw: Whether to draw to a window on the screen
            save: Whether to save to file in out_dir
            out_dir: Where to write output, if any
            output_format: Format of the output file
        """
        
        self._draw_ecm(par_pos, par_type, bond_groups)
        self._draw_pde(pde)
        self._draw_cpm(cpm)
        self._draw_act(actfield)

        if save:
            if out_dir is None:
                raise RuntimeError('Trying to save image, but no out_dir specified')
            file_name = str(out_dir / f'state_{i:05d}.{output_format}')
            self._fig.savefig(file_name, format=output_format, dpi=self._dpi)

        if draw:
            plt.draw()
            plt.show(block=False)
            plt.pause(0.000001)

    def _draw_ecm(
            self, par_pos: npt.NDArray[np.float64], par_type: npt.NDArray[np.int32],
            bond_groups: npt.NDArray[np.int32]) -> None:
        """Update the ECM part of the diagram

        Args:
            par_pos: Particle positions as an Nx2 array
            par_type: Particle types as an N-vector
            bond_groups: Ids of bonded particles, Mx2 array
        """
        pos_x = par_pos[:, 0]
        pos_y = par_pos[:, 1]

        # Removing duplicated items from bond_groups.
        # This avoids redrawing fibers on the edges of different domains 
        # in parallel simulations
        unique_dic  = {}
        for i in range(len(bond_groups)):
            unique_dic[tuple(sorted(bond_groups[i,:]))] = i # type: ignore[type-var]
        bond_groups =  np.array(list(unique_dic.keys()))

        _logger.debug(f'bond_groups: {len(bond_groups)}')
        _logger.debug(f'bond_lines: {len(self._bond_lines)}')
        for i in range(len(bond_groups)):
            x = [pos_x[bond_groups[i, 0]], pos_x[bond_groups[i, 1]]]
            y = [pos_y[bond_groups[i, 0]], pos_y[bond_groups[i, 1]]]
            if i < len(self._bond_lines):
                self._bond_lines[i].set_data(x, y)
                self._bond_lines[i].set_visible(True)
            else:
                line, = plt.plot(x, y, '-', color='#40597F', alpha=0.8, linewidth= 0.5)
                self._bond_lines.append(line)

        # Hide bond_lines that are not in the bond_groups.
        if len(self._bond_lines) > len(bond_groups):
            for i in range(len(bond_groups),len(self._bond_lines)):
                self._bond_lines[i].set_visible(False)

        adhesions = par_pos[par_type == ParticleType.adhesion.value]
        self._adhesion_marks.set_data(adhesions[:, 0], adhesions[:, 1])
        self._adhesion_marks.set_color('#0BAA00')

    def _draw_pde(self, pde: npt.NDArray[np.float64]) -> None:
        """Update the PDE part of the diagram

        Args:
            pde: Concentrations, L x SizeX x SizeY array
        """
        if self._pde_image:
            self._pde_image.remove()

        self._pde_image = plt.imshow(
                pde[0], origin = 'upper', cmap = matplotlib.colormaps['hot_r'])

    def _draw_act(self, actfield: dict) -> None:
        """Update the ACT part of the diagram

        Args:
            actfield: Act level, SizeX x SizeY array
        """
        if self._act_image:
            self._act_image.remove()

        # Converting the dictonary data into an integer grid
        act_grid= np.zeros((self._sizey,self._sizex),dtype=int)
        for key in actfield.keys():
            comma_loc = key.find(',')
            i = int(key[:comma_loc])
            j = int(key[comma_loc+1:])
            act_grid[j,i] = actfield[key]

        self._act_image = plt.imshow(
                act_grid, origin = 'upper', cmap = matplotlib.colormaps['hot_r'])

    def _draw_cpm(self, cpm: npt.NDArray[np.int32]) -> None:
        """Update the CPM state part of the diagram

        Args:
            cpm: Cellular Potts state, SizeX x SizeY array
        """
        if self._cpm_contours:
                self._cpm_contours.remove()

        if self._cpm_contour_fill:
            self._cpm_contour_fill.remove()

        # this skips the contour at the edge, between -1 and 0
        levels = np.array([0.5, np.max(cpm) + 0.5])
        self._cpm_contour_fill = plt.contourf(
                self._cpm_grid[0], self._cpm_grid[1], cpm, levels = levels,
                alpha = 0.5, colors = '#CDAECD')

        self._cpm_contours = plt.contour(
                self._cpm_grid[0], self._cpm_grid[1], cpm,
                alpha = 1, colors = ['#A16EA1'], linewidths = 0.1,
                antialiased = False, zorder = 2.05)
