"""Model state viewer

Based on artist.py in TST-MD
"""
import logging
from pathlib import Path
from typing import List, Optional

# import matplotlib.cm as cm
# from matplotlib.contour import QuadContourSet
# from matplotlib.image import AxesImage
# from matplotlib.lines import Line2D
# import matplotlib.pyplot as plt

import PyQt5
import pyqtgraph as pg

import numpy as np
import numpy.typing as npt

from tissue_simulation_toolkit.ecm.ecm import ParticleType


_logger = logging.getLogger(__name__)


# I took this color map as the first 10 values from default.ctb in TST/data.
# I changed some of the alpha values to make them look nicer.
_color_map = {
    'pos': [0,1],
    'color': [
        [254, 254, 254, 0],
#        [  0,   0,   0, 150],
        [254,   0,   0, 150],
#        [254, 254,   0, 150],
#        [  0,   0, 254, 150],
#        [255,   0, 255, 150],
#        [  0, 255, 255, 150],
#        [  0, 255,   0, 150],
#        [ 85,  85,  85, 150],
#        [198, 113, 113, 150],
#        [113, 198, 113, 150],
        ]
}



    

class QtStatePlotter:
    """Plots the simulation state on the screen or to a PNG."""
    def __init__(self, Lx: float, Ly: float, img_height: int = 480) -> None:
        """Create a Viewer

        Image width will be set automatically based on the height and the Lx/Ly
        aspect ratio.

        Args:
            Lx: Half-length in the x direction of the model domain
            Ly: Half-length in the y direction of the model domain
            img_height: Height of the image in pixels
        """
        self._Lx = Lx
        self._Ly = Ly
        self._img_height = img_height
        self._img_width = int(img_height * Lx / Ly)
        self._dpi = 100.0
        offset = 0.0

        self._figsize = (self._img_width / self._dpi, self._img_height / self._dpi)
        
        self._plotwidget = pg.plot(title="I should put a more descriptive title")

        viewbox = self._plotwidget.getViewBox() 
        viewbox.setAspectLocked(lock=True, ratio=1)
        viewbox.setDefaultPadding(padding=0)
        
        viewbox.setFixedWidth(self._img_width)
        viewbox.setFixedHeight(self._img_height) 
        
        # Disable auto-ranging
        self._plotwidget.enableAutoRange(x=False, y=False)

        self._plotwidget.hideAxis("left")
        self._plotwidget.hideAxis("bottom")
        self._plotwidget.hideAxis("right")
        self._plotwidget.hideAxis("top")

        self._plotwidget.setBackground("white")
        self._plotwidget.setXRange(-offset, offset + 2*self._Lx)
        
        # flip y-axis to match TST graphics
        self._plotwidget.setYRange(-offset, 2*self._Ly + offset)
        self._plotwidget.invertY()

    def draw(
            self, i: int, par_pos: npt.NDArray[np.float64],
            par_type: npt.NDArray[np.int32], bond_groups: npt.NDArray[np.int32], 
            bond_types: npt.NDArray[np.int32], pde: npt.NDArray[np.float64], 
            cpm: npt.NDArray[np.int32],
            draw: bool = True, save: bool = True, out_dir: Optional[Path] = None
            ) -> None:
        """Update the diagram with new data

        Args:
            par_pos: Particle positions as an Nx2 array
            par_type: Particle types as an N-vector
            bond_groups: Ids of bonded particles, Mx2 array
            pde: Concentrations, L x SizeX x SizeY array
            cpm: Cellular Potts state, SizeX x SizeY array
            draw: Whether to draw to a window on the screen
            save: Whether to save to file in out_dir
            out_dir: Where to write output, if any
        """
        self._plotwidget.clear()
        self._draw_ecm(par_pos, par_type, bond_groups, bond_types)
        self._draw_pde(pde)
        self._draw_cpm(cpm)

        if save:
            if out_dir is None:
                raise RuntimeError('Trying to save image, but no out_dir specified')
            file_name = str(out_dir / f'state_{i:05d}.png')
            self._plotwidget.writeImage(file_name)

        if draw:
            pass
        
    def _draw_bonds(self, par_pos, bond_groups, color):
        pos_x = par_pos[:, 0]
        pos_y = par_pos[:, 1]
        
        flat_bonds = bond_groups.reshape(-1)
        
        frame_x = pos_x[flat_bonds]
        frame_y = pos_y[flat_bonds]
        
        path = pg.arrayToQPath(frame_x, frame_y, connect='pairs')
        p = pg.QtWidgets.QGraphicsPathItem(path)
        p.setPen(pg.mkPen(color))
        self._plotwidget.addItem(p)

    def _draw_ecm(
            self, par_pos: npt.NDArray[np.float64], par_type: npt.NDArray[np.int32],
            bond_groups: npt.NDArray[np.int32], bond_types: npt.NDArray[np.int32]) -> None:
        """Update the ECM part of the diagram

        Args:
            par_pos: Particle positions as an Nx2 array
            par_type: Particle types as an N-vector
            bond_groups: Ids of bonded particles, Mx2 array
        """

        polymer_group = bond_groups[bond_types == 0]
        self._draw_bonds(par_pos, polymer_group, 'black')
        
        crosslink_group = bond_groups[bond_types > 0]
        self._draw_bonds(par_pos, crosslink_group, 'green')
        
        self._draw_adhesions(par_pos, par_type)
    
    def _draw_adhesions(
        self, par_pos: npt.NDArray[np.float64], par_ids: npt.NDArray[np.int32]):
        
        pos_x = par_pos[:, 0]
        pos_y = par_pos[:, 1]
        
        adhesions_indices = par_ids == ParticleType.adhesion.value

        frame_x = pos_x[adhesions_indices] 
        frame_y = pos_y[adhesions_indices] 
        
        color = pg.mkColor('blue')
        spi = pg.ScatterPlotItem(frame_x, frame_y, pen=color, brush=color, alpha=0.5,
                                 size = 2)

        self._plotwidget.addItem(spi)

    def _draw_pde(self, pde: npt.NDArray[np.float64]) -> None:
        """Update the PDE part of the diagram

        Args:
            pde: Concentrations, L x SizeX x SizeY array
        """
        pass

    def _draw_cpm(self, cpm: npt.NDArray[np.int32]) -> None:
        """Update the CPM state part of the diagram

        Args:
            cpm: Cellular Potts state, SizeX x SizeY array
        """
        
        def _cell_color_function(spin: int) -> int:
            """Turns the spin into an index of _color_map.
        
            Should be a function of the type of cell as well, but I don't have acces to this"""
            if spin <= 0:
                return 0.0
            return 2.0 / 11.0
        cpm[cpm <= 0] = 0
        cpm[cpm > 0] = 1

        image = pg.ImageItem()

        image.setImage(cpm)

        colormap = pg.ColorMap(
                _color_map["pos"],
                _color_map["color"],
                mode='clip')
        image.setColorMap(colormap)
        self._plotwidget.addItem(image)

 