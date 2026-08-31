"""Script that plots saved states

"""
from argparse import ArgumentParser, Namespace
from pathlib import Path
import pickle
from typing import Optional

from tissue_simulation_toolkit.cpm_ecm.state_plotter import StatePlotter


def find_data_dir(input_dir_str: str) -> Path:
    """Gets the correct path given the user-passed directory."""
    input_dir = Path(input_dir_str)
    if not input_dir.exists():
        raise RuntimeError(
                'The given directory does not exist. Please pass a run directory'
                'or the work directory of the dumper')

    work_dir = input_dir / 'instances' / 'state_dumper' / 'workdir'
    if work_dir.exists():
        return work_dir
    return input_dir


def parse_args() -> Namespace:
    """Gets an input directory from the command line arguments"""
    parser = ArgumentParser(description='Plot CPM/ECM states')
    parser.add_argument('dir', type=str, help='Path to run dir or workdir')
    parser.add_argument(
            '--image-height', type=int, default=600,
            help='Height of the image in pixels')
    parser.add_argument('--output-format', type=str,
                        default='png',help = 'Format of the output files (should be compatible with matplotlib.pyplot.savefig)')
    args = parser.parse_args()
    return args


def main() -> None:
    args = parse_args()
    data_dir = find_data_dir(args.dir)
    FMT = args.output_format

    files = sorted([
            Path(f) for f in data_dir.iterdir()
            if f.is_file() and f.name.endswith('.pickle')])

    plotter: Optional[StatePlotter] = None

    for data_file in files:
        if data_file.with_suffix('.' + FMT).exists():
            continue

        with data_file.open('rb') as f:
            data = pickle.load(f)

        mcs = data['mcs']
        sizex = data['sizex']
        sizey = data['sizey']
        print(f'mcs: {mcs}')

        if plotter is None:
            plotter = StatePlotter(sizex, sizey, args.image_height)
            set_sizex = sizex
            set_sizey = sizey
        else:
            if sizex != set_sizex or sizey != set_sizey:
                raise RuntimeError(f'Domain size changed when loading {data_file}')

        particles = data['ecm_state']['particles']

        plotter.draw(
                mcs,
                particles['positions'].array,
                particles['types'].array,
                data['ecm_state']['bonds']['groups'].array,
                data['cpm_state']['pde'].array,
                data['cpm_state']['cpm'].array,
                data['cpm_state']['act_field'],
                draw=False, save=True, out_dir=data_dir,
                output_format=FMT)

if __name__ == '__main__':
    main()
