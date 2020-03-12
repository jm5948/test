import logging

from opensfm import dataset
from opensfm import dense

logger = logging.getLogger(__name__)


class Command:

    def run(self, args):
        data = dataset.DataSet(args)
        udata = dataset.UndistortedDataSet(data, 'undistorted')
        data.config['interactive'] = args
        reconstructions = udata.load_undistorted_reconstruction()
        graph = udata.load_undistorted_tracks_graph()

        dense.compute_depthmaps(udata, graph, reconstructions[0])
