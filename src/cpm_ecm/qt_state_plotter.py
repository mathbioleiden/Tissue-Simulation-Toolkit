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
from pyqtgraph.exporters import Exporter

import numpy as np
import numpy.typing as npt

from tissue_simulation_toolkit.ecm.ecm import ParticleType


_logger = logging.getLogger(__name__)


# I took this color map as the first 10 values from default.ctb in TST/data.
# I changed some of the alpha values to make them look nicer.
_color_map = [
    [254, 254, 254, 0],  # wit
    [0, 0, 0, 254],  # zwart
    [254, 0, 0, 150],  # rood
    # [254, 254, 0, 150],
    [0, 0, 254, 150],
    [255, 0, 255, 150],
    [0, 255, 255, 150],
    [0, 255, 0, 150],
    [85, 85, 85, 150],
    [198, 113, 113, 150],
    [113, 198, 113, 150],
]


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
        PyQt5.QtWidgets.QApplication.setStyle("Fusion") 
        

        

        self._Lx = Lx
        self._Ly = Ly
        self._img_height = img_height
        self._img_width = int(img_height * Lx / Ly)
        self._image_scale = 2
        self._dpi = 1.0
        offset = 0.0

        self._figsize = (
             int(self._image_scale*self._img_width / self._dpi),
             int(self._image_scale*self._img_height / self._dpi),
        )
        
        # app = pg.mkQApp()
        self._plotwidget = pg.plot(title="I should put a more descriptive title")

        # self.mainwindow = PyQt5.QtWidgets.QMainWindow()
        # self.mainwindow.setGeometry(0,0, self._figsize[0], self._figsize[1])
        # self.mainwindow.setCentralWidget(self._plotwidget)

        view = self._plotwidget.getPlotItem().getViewWidget()
        view.setFixedWidth(self._figsize[0])
        view.setFixedHeight(self._figsize[1])
        # view.setAspectLocked(lock=True, ratio=1)
        # viewbox = self._plotwidget.getViewBox()
        # viewbox.setAspectLocked(lock=True, ratio=1)
        # viewbox.setDefaultPadding(padding=0)

        # viewbox.setFixedWidth(self._figsize[0])
        # viewbox.setFixedHeight(self._figsize[1])

        # Disable auto-ranging
        # self._plotwidget.enableAutoRange(x=False, y=False)

        self._plotwidget.hideAxis("left")
        self._plotwidget.hideAxis("bottom")
        self._plotwidget.hideAxis("right")
        self._plotwidget.hideAxis("top")

        self._plotwidget.setBackground("white")
        self._plotwidget.getPlotItem().setXRange(0, self._image_scale*2*self._Lx, padding=0.0)

        # flip y-axis to match TST graphics
        # self._plotwidget.setYRange(-offset*self._image_scale,self._image_scale*( 2 * self._Ly + offset))
        self._plotwidget.getPlotItem().setYRange(0, self._image_scale*2*self._Ly,padding=0.0)
        #self._plotwidget.invertY()

    def draw(
        self,
        i: int,
        par_pos: npt.NDArray[np.float64],
        par_type: npt.NDArray[np.int32],
        bond_groups: npt.NDArray[np.int32],
        bond_types: npt.NDArray[np.int32],
        pde: npt.NDArray[np.float64],
        cpm: npt.NDArray[np.int32],
        adh,
        act = None,
        draw: bool = True,
        save: bool = True,
        out_dir: Optional[Path] = None,
        colour_options = None,
        tipcell = None,
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
        self._draw_pde(pde)
        self._draw_cpm(cpm, tipcell=tipcell, colour_options=colour_options)
        self._draw_ecm(par_pos, par_type, bond_groups, bond_types)
        self._draw_adhesions(par_pos, par_type, adh)
        
        if act:
            self._draw_act(act)

        if save:
            if out_dir is None:
                raise RuntimeError("Trying to save image, but no out_dir specified")
            file_name = str(out_dir / f"state_{i:05d}.png")
            exporter = pg.exporters.ImageExporter(self._plotwidget.getPlotItem())
            
            
            # set export parameters if needed
            # exporter.parameters()['aspectratio'] = 1.0
            exporter.parameters()['width'] = self._figsize[0]
            # self._plotwidget.writeImage(file_name)
            exporter.export(file_name)

        if draw:
            pass

    def _draw_bonds(self, par_pos, bond_groups, color, width=1):
        pos_x = self._image_scale * par_pos[:, 0]
        pos_y = self._image_scale * par_pos[:, 1]

        flat_bonds = bond_groups.reshape(-1)

        frame_x = pos_x[flat_bonds]
        frame_y = pos_y[flat_bonds]

        path = pg.arrayToQPath(frame_x, frame_y, connect="pairs")
        p = pg.QtWidgets.QGraphicsPathItem(path)
        p.setPen(pg.mkPen(color, width=width))
        self._plotwidget.addItem(p)

    def _draw_ecm(
        self,
        par_pos: npt.NDArray[np.float64],
        par_type: npt.NDArray[np.int32],
        bond_groups: npt.NDArray[np.int32],
        bond_types: npt.NDArray[np.int32],
    ) -> None:
        """Update the ECM part of the diagram

        Args:
            par_pos: Particle positions as an Nx2 array
            par_type: Particle types as an N-vector
            bond_groups: Ids of bonded particles, Mx2 array
        """

        polymer_group = bond_groups[bond_types == 0]
        self._draw_bonds(par_pos, polymer_group, "black")

        crosslink_group = bond_groups[bond_types > 0]
        self._draw_bonds(par_pos, crosslink_group, "green", width=3)

    def _draw_adhesions(
        self,
        par_pos: npt.NDArray[np.float64],
        par_ids: npt.NDArray[np.int32],
        adh,
    ):
        pos_x = self._image_scale * par_pos[:, 0]
        pos_y = self._image_scale * par_pos[:, 1]

        (adhesions_indices,) = np.where(par_ids == ParticleType.adhesion.value)

        frame_x = pos_x[adhesions_indices]
        frame_y = pos_y[adhesions_indices]
        if adh:
            tensions = [
                adh.get(str(i), {"tension": 0.0})["tension"] for i in adhesions_indices
            ]
            integrins = [
                adh.get(str(i), {"size": 0.0})["size"] for i in adhesions_indices
            ]
            myosin = [
                adh.get(str(i), {"myosin": 0.0})["myosin"] for i in adhesions_indices
            ]
            # colors = [pg.mkColor((255, 255, tension)) for tension in tensions]
            colors = [(0, 255, 255 * (1-m)) for m in myosin]
            print(colors)

            sizes = [self._image_scale*2*i / 50 for i in integrins]
        else:
            colors = "yellow" # type: ignore
            sizes = self._image_scale*2 # type: ignore
            print("Warning: Not loaded adhesion data")

        spi = pg.ScatterPlotItem(
            frame_x, frame_y, pen=colors, brush=colors, alpha=0.5, size=sizes
        )

        self._plotwidget.addItem(spi)

    def _draw_pde(self, pde: npt.NDArray[np.float64]) -> None:
        """Update the PDE part of the diagram

        Args:
            pde: Concentrations, L x SizeX x SizeY array
        """
        def _pde_color_function(layer: int):
            return _color_map[-1]

    def _draw_cpm(self, cpm: npt.NDArray[np.int32], colour_options=None, tipcell=None) -> None:
        """Update the CPM state part of the diagram

        Args:
            cpm: Cellular Potts state, SizeX x SizeY array
        """

        def _cell_color_function(spin: int):
            """Turns the spin into an index of _color_map.

            Should be a function of the type of cell as well, but I don't have acces to this
            """
            if spin < 0:
                return _color_map[1]
            if spin == 0:
                return _color_map[0]
            if colour_options and tipcell:
                if tipcell == spin:
                    return _color_map[colour_options['tipcell']]
                else:
                    return _color_map[colour_options['cell']]
            return _color_map[2 + spin % (len(_color_map) - 2)]

        image_scale = self._image_scale
        image_data = np.zeros(
            (image_scale * 2 * int(self._Lx), image_scale * 2 * int(self._Ly), 4)
        )
        for spin in np.unique(cpm):
            color = _cell_color_function(spin)
            indices = np.where(cpm == spin)
            image_data[indices[0], indices[1], :] = color
            image_data[indices[0] + 1, indices[1] + 1, :] = color
            image_data[indices[0], indices[1] + 1, :] = color
            image_data[indices[0] + 1, indices[1], :] = color

        # contours:
        contour_color = _cell_color_function(-1)

        # left neighbour
        neighbours = np.where(np.logical_and(cpm != 0, np.roll(cpm, +1, axis=0) != cpm))
        image_data[neighbours[0], neighbours[1], :] = contour_color
        image_data[neighbours[0], neighbours[1] + 1, :] = contour_color

        # right neighbour
        neighbours = np.where(np.logical_and(cpm != 0, np.roll(cpm, -1, axis=0) != cpm))
        image_data[neighbours[0] + 1, neighbours[1], :] = contour_color
        image_data[neighbours[0] + 1, neighbours[1] + 1, :] = contour_color

        # up neighbour
        neighbours = np.where(np.logical_and(cpm != 0, np.roll(cpm, -1, axis=1) != cpm))
        image_data[neighbours[0], neighbours[1] + 1, :] = contour_color
        image_data[neighbours[0] + 1, neighbours[1] + 1, :] = contour_color

        # down neighbour
        neighbours = np.where(np.logical_and(cpm != 0, np.roll(cpm, +1, axis=1) != cpm))
        image_data[neighbours[0], neighbours[1], :] = contour_color
        image_data[neighbours[0] + 1, neighbours[1], :] = contour_color

        image = pg.ImageItem()
        image.setImage(image_data)
        #image.setImage(cpm)
        image.setRect(0, 0, self._Lx * 8, self._Ly * 8)
        #image.setRect(0, 0, self._image_scale*2*int(self._Lx), self._image_scale*2*int(self._Ly))
        
        self._plotwidget.addItem(image)
        
    def _draw_act(self, act):
        X = [] 
        Y = []
        colors = []
        for pos, value in act.items():
            X.append(self._image_scale * int(pos.split(',')[0]))
            Y.append(self._image_scale * int(pos.split(',')[1]))
            color = 255 * ( 1 - value / 15) # 15 is act_Max
            colors.append(
                pg.mkColor((color,color,color))
            )

        spi = pg.ScatterPlotItem(
            X, Y, pen=colors, brush=colors, alpha=0.5, size=5
        )
        self._plotwidget.addItem(spi)

    """
    """
