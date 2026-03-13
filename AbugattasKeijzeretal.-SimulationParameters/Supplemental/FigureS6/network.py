import pandas as pd
import itertools
import seaborn as sns
from PIL import Image
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from plot_makeup import savefile, figure_options, no_borders, no_legend, significance, flip_yaxis
from scipy.stats import ttest_ind
from TST_analyse import Simulation
from TST_analyse.graphics.qtartistwrapper import CellsCanvas_artist
from TST_analyse.graphics.qtartist import DrawOptions
from TST_analyse import put_stars  # as put_stars_non_corrected
from PIL import Image

DATADIR = Path("../data/networks").resolve()
FIGUREDIR = Path("../figures/network").resolve()
SUPFIGUREDIR = Path("../figures/network/sup/").resolve()
SCRATCH = Path("../scratch/networks").resolve()

sns.set_palette(sns.color_palette("colorblind"))


def make_screenshot(sim, time, fig, ax, what_to_draw):
    options = dict(
        adh=dict(
            draw_nascent_adhesions=False,
            minimal_adhesion_size=50,
            maximal_adhesion_size=390,
        ),
        poly=dict(
            color="black", #kwargs["fiber_color"],
            width=1 ,
        ),
        cross=dict(
            color="green",
            width=1,
        ),
        pde=dict(layer=0),
        tipcell=False,
        cell_color='red',
        equal=True,
    )



    outputfile = SCRATCH / "temp.png"
    artist = CellsCanvas_artist(sim)
    artist.drawFromDict(time, what_to_draw ,options)
    artist.store(outputfile)

    image = Image.open(outputfile)
    shape_x, shape_y = image.size

    # cropped_image = image.crop((shape_x / 4, 0, 3 * shape_x / 4, shape_y - 1))
    ax.imshow(image)



def screenshots():
    
    files = [DATADIR / f"20250513-meco/data_isv_initFalsen_init_cells100size_init_cells800sizex400sizey400Lx200_0Ly200_0box_size_x400box_size_y400mcs5000strands1num_init_crosslinks48000it{it}" for it in [1,2,3] ]

    what_to_draw = {
        "cell": True,
        "poly": False,
        "cross": False,
        "adh": True,
        "act": False,
        "pde": False,
    }

    for it, file in enumerate(files):
        sim = Simulation(file)
        max_time = max(sim.times)
        print(sim.times)

        @savefile(file=FIGUREDIR / f"screenshot_{it+1}.png", dpi=300)
        @no_borders
        def plot(fig, ax):
            make_screenshot(sim, max_time, fig,ax, what_to_draw)
        plot()

    files = list( (DATADIR/ "20250602-meco/soft/").glob("data_*") )

    what_to_draw = {
        "cell": True,
        "poly": True,
        "cross": True,
        "adh": False,
        "act": False,
        "pde": False,
    }

    for it, file in enumerate(files):
        sim = Simulation(file)
        max_time = max(sim.times)
        print(file.stem)
        @savefile(file=FIGUREDIR / f"{file.stem}.png", dpi=300)
        @no_borders
        def plot(fig, ax):
            make_screenshot(sim, max_time, fig,ax, what_to_draw)
        plot()

def figugue_sema():
    def load_data():
        df1= pd.read_feather( DATADIR / "20250624-meco/crossings.feather")
        df2=pd.read_feather( DATADIR / "20250630-camb/crossings.feather")
        df2['it'] += df1['it'].max()

        df1 = df1[df1['adhesion_contraction_force'] == 2.0].reset_index(drop=True)

        df = pd.concat([df1, df2])
        print(df)
        return df
    data = load_data()
    data['crossing_percent'] = 100 * (data['crossings'] / 10.0)
    final = (
            data
            .query("time == 10000")
            [['diff_coeff_0', 'spring_k', 'crossing_percent', 'it']]
            .pivot_table(index='spring_k', columns='diff_coeff_0', values='crossing_percent', aggfunc='mean')
        )
    
    @savefile(file=FIGUREDIR / "crossings_heatmap.png", dpi=300)
    def plot(fig, ax):
    # Use a perceptually uniform colormap (e.g., 'mako', 'viridis', 'rocket')
        sns.heatmap(
            final,
            cmap='viridis',       # Choose a smooth, continuous colormap
            cbar_kws={'label': 'Mean value'},
            square=True,          # Force square cells
            linewidths=0.5,       # Optional: thin gridlines
            linecolor='white',
            xticklabels=True,
            yticklabels=True,
            annot=True,
        )
    
        plt.xlabel("diff_coeff_0")#, fontsize=12)
        plt.ylabel("spring_k")#, fontsize=12)

    @savefile(file=FIGUREDIR / "crossings_time_diff2.png", dpi=300)
    def timeplot(fig, ax):
    # Use a perceptually uniform colormap (e.g., 'mako', 'viridis', 'rocket')
        sns.lineplot(
            data=data.query("diff_coeff_0 == 2.0"),
            x='time',
            y='crossings',
            hue= 'spring_k',
            errorbar='sd',
            legend=None,
        )

    @savefile(file=FIGUREDIR / "crossings_barplot.png", dpi=300)
    def timeplot(fig, ax):
    # Use a perceptually uniform colormap (e.g., 'mako', 'viridis', 'rocket')
        sns.lineplot(
            data=data.query("time == 10000"),
            x='diff_coeff_0',
            y='crossing_percent',
            hue= 'spring_k',
            errorbar='sd',
            legend=None,
        )
        # sns.scatterplot(
        #     data=data.query("time == 10000"),
        #     x='diff_coeff_0',
        #     y='crossing_percent',
        #     hue= 'spring_k',
        #     legend=None,
        # )

    with plt.rc_context({"font.size": 20}):
        plot()
        timeplot()
    

def screenshots_sema_video():
    files = (DATADIR / f"20250624-meco").glob("data_sizex633box_size_x633Lx316_5number_of_ISV10strands600spring_k50_0Ly100_0box_size_y200sizey200adhesion_contraction_force2_0adhesion_yielding_lambda100only_tipcell_adhTruesomite_antitaxis100diff_coeff1_0,1e-13it*")

    what_to_draw = {
        "cell": True,
        "poly": True,
        "cross": True,
        "adh": True,
        "act": False,
        "pde": False,
    }
    
    for file in files:
        sim = Simulation(file)
        output_folder = FIGUREDIR / "sema_video"
        output_folder.mkdir(exist_ok=True)
        for time in sorted(sim.times)[1:]:
            @savefile(file=output_folder / f"{file.stem}_{time}.png", dpi=300)
            @no_borders
            @flip_yaxis
            def plot(fig, ax):
                make_screenshot(sim, time, fig,ax, what_to_draw)
            plot()

def screenshots_sema():
    from itertools import chain 
    files = chain( (DATADIR / f"20250630-camb/").glob("data_*"), (DATADIR / f"20250624-meco/").glob("data_*adhesion_contraction_force2_0*") )

    what_to_draw = {
        "cell": True,
        "poly": True,
        "cross": True,
        "adh": True,
        "act": False,
        "pde": False,
    }

    for it, file in enumerate(files):
        sim = Simulation(file)
        spring_k = sim.Parameter("spring_k")
        diffcoef = sim.Parameter("diff_coeff")[0]
        it = sim.Parameter("it")
        output_folder = FIGUREDIR / "sema"
        output_folder.mkdir(exist_ok=True)
        time = max(sim.times)
        @savefile(file=output_folder / f"{spring_k}_{diffcoef}_{it}.png", dpi=300)
        @no_borders
        @flip_yaxis
        def plot(fig, ax):
            make_screenshot(sim, time, fig,ax, what_to_draw)
        plot()

def screenshots_sema_2():
    from itertools import chain 
    files = chain( (DATADIR / f"20250630-meco/").glob("data_*") )

    what_to_draw = {
        "cell": True,
        "poly": True,
        "cross": True,
        "adh": True,
        "act": False,
        "pde": False,
    }

    for it, file in enumerate(files):
        sim = Simulation(file)
        spring_k = sim.Parameter("spring_k")
        diffcoef = sim.Parameter("diff_coeff")[0]
        it = sim.Parameter("it")
        output_folder = FIGUREDIR / "sema_meco"
        output_folder.mkdir(exist_ok=True)
        time = max(sim.times)
        @savefile(file=output_folder / f"{spring_k}_{diffcoef}_{it}.png", dpi=300)
        @no_borders
        @flip_yaxis
        def plot(fig, ax):
            make_screenshot(sim, time, fig,ax, what_to_draw)
        plot()


def screenshot_movies():
    file = DATADIR / "20250610-meco/data_number_of_ISV3only_tipcell_adhTrueadhesion_contraction_force1adhesion_yielding_lambda100spring_k50_0it3"
    sim = Simulation(file)

    what_to_draw = {
        "cell": True,
        "poly": True,
        "cross": True,
        "adh": True,
        "act": False,
        "pde": False,
    }
    outfolder = FIGUREDIR / f"610-meco-spring_k50it3/"
    outfolder.mkdir(exist_ok=True)
    for time in itertools.chain([100],  range(0, 10001, 1000)):
        @savefile(file=outfolder / f"frame_{str(time).zfill(7)}.jpg", dpi=300)
        @no_borders
        def plot(fig, ax):
            make_screenshot(sim, time, fig, ax, what_to_draw)
        plot()

def ISV_no_cell():
    what_to_draw = {
        "cell": False,
        "poly": True,
        "cross": True,
        "adh": False,
        "act": False,
        "pde": False,
    }
    sim = Simulation( DATADIR/ "20250602-meco/soft/data_mcs10001state_output_interval50number_of_ISV3only_tipcell_adhTruesecr_rate0_0,0_00018diff_coeff1e-12,1e-13strands300spring_k100_0adhesion_contraction_force1it1")

    @savefile(file=FIGUREDIR / f"isv_no_cell.jpg", dpi=300)
    @no_borders
    def plot_no_cell(fig, ax):
        make_screenshot(sim, 0, fig, ax, what_to_draw)

    plot_no_cell()

def ISV_cell():
    what_to_draw = {
        "cell": True,
        "poly": True,
        "cross": True,
        "adh": True,
        "act": False,
        "pde": False,
    }
    files = ( DATADIR/ "20250610-meco/").glob("data_*")
    for file in files:
        sim = Simulation(file)
        name = file.stem
        (FIGUREDIR / "isv").mkdir(exist_ok=True)
        time = max(sim.times)

        @savefile(file=FIGUREDIR / f"isv/{name}.jpg", dpi=300)
        @no_borders
        def plot(fig, ax):
            make_screenshot(sim, time, fig, ax, what_to_draw)
        plot()

def ISV_cell_large():
    what_to_draw = {
        "cell": True,
        "poly": True,
        "cross": True,
        "adh": True,
        "act": False,
        "pde": False,
    }
    files = ( DATADIR/ "20250624-meco/").glob("data_*")
    for file in files:
        sim = Simulation(file)
        name = file.stem
        (FIGUREDIR / "isv_large").mkdir(exist_ok=True)
        time = max(sim.times)

        @savefile(file=FIGUREDIR / f"isv_large/{name}.jpg", dpi=300)
        @no_borders
        def plot(fig, ax):
            make_screenshot(sim, time, fig, ax, what_to_draw)
        plot()




def main():
    DATADIR.mkdir(exist_ok=True)
    FIGUREDIR.mkdir(exist_ok=True)
    SUPFIGUREDIR.mkdir(exist_ok=True)
    SCRATCH.mkdir(exist_ok=True)

    # screenshot_movies()
    # ISV_cell()
    # ISV_cell_large()
    # screenshots_sema()
    screenshots_sema_2()
    # screenshots_sema_video()
    # figugue_sema()

    # screenshots()
    # ISV_no_cell()


if __name__ == "__main__":
    main()
