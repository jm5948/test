import open3d as o3d
import os

class Command:
    def run(self, args):
        image_path = args
        print(image_path)
        path_name2 = image_path + '/undistorted/depthmaps/merged.ply'

        print(path_name2)
        print(path_name2)
        print(path_name2)

        # /Users/chaejaemin/Downloads/opensfm/OpenSfM/data/lund/undistorted/depthmaps/merged.ply
        pcd = o3d.io.read_point_cloud(path_name2)
        o3d.visualization.draw_geometries([pcd])