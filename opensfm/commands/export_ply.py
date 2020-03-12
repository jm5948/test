import logging
import os

import numpy as np

from opensfm import dataset, io
from opensfm.dense import depthmap_to_ply, scale_down_image

logger = logging.getLogger(__name__)


class Command:
    name = 'export_ply'
    help = "Export reconstruction to PLY format"

    def add_arguments(self, parser):
        parser.add_argument('dataset', help='dataset to process')
        parser.add_argument('--no-cameras',
                            action='store_true',
                            default=False,
                            help='Do not save camera positions')
        parser.add_argument('--no-points',
                            action='store_true',
                            default=False,
                            help='Do not save points')
        parser.add_argument('--depthmaps',
                            action='store_true',
                            default=False,
                            help='Export per-image depthmaps as pointclouds')

    def run(self, args):
        data = dataset.DataSet(args)
        reconstructions = data.load_reconstruction()
        no_cameras = False
        no_points = False

        if reconstructions:
            data.save_ply(reconstructions[0], None, no_cameras, no_points)

"""        if args.depthmaps and reconstructions:
            udata = dataset.UndistortedDataSet(data, 'undistorted')
            for id, shot in reconstructions[0].shots.items():
                rgb = udata.load_undistorted_image(id)
                for t in ('clean', 'raw'):
                    path_depth = udata._depthmap_file(id, t + '.npz')
                    if not os.path.exists(path_depth):
                        continue
                    depth = np.load(path_depth)['depth']
                    rgb = scale_down_image(rgb, depth.shape[1], depth.shape[0])
                    ply = depthmap_to_ply(shot, depth, rgb)
                    with io.open_wt(udata._depthmap_file(id, t + '.ply')) as fout:
                        fout.write(ply)
                        """
