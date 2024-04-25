#ply file analysis
import numpy as np
from plyfile import PlyData
from typing import NamedTuple
import trimesh


given_path = "../dataset/360_v2/bicycle/test2/sparse/0/points3D.ply"
example_path = "../dataset/360_v2/bicycle/test6/dust3r/scene.glb"
pointcloud_path = "../dataset/360_v2/bicycle/test6/dust3r/pointcloud.ply"

class BasicPointCloud(NamedTuple):
    points : np.array
    colors : np.array
    normals : np.array

def fetchPly(path):
    plydata = PlyData.read(path)
    vertices = plydata['vertex']
    positions = np.vstack([vertices['x'], vertices['y'], vertices['z']]).T
    colors = np.vstack([vertices['red'], vertices['green'], vertices['blue']]).T / 255.0
    normals = np.vstack([vertices['nx'], vertices['ny'], vertices['nz']]).T
    print("positions.shape: ", positions.shape)
    print("colors.shape: ", colors.shape)
    print("normals.shape: ", normals.shape)
    print("positions: ", positions)
    print("colors: ", colors)
    print("normals: ", normals)
    return BasicPointCloud(points=positions, colors=colors, normals=normals)

def fetchGlb(path):
    scene = trimesh.load(path, process=False)
    # print("Scene: ", scene)
    # print("color: ", scene.colors)
    print("Scene: ", scene)
    mesh = scene.geometry
    #ordered dictionary each key print
    # for key in mesh:
    #     print(f"Key: {key}")
    #     print(f"Geometry Type: {type(mesh[key])}")
    #     print(f"Geometry: {mesh[key]}")
    
    #extract pointcloud (pose)
    for key in mesh:
        if type(mesh[key]) == trimesh.PointCloud:
            #extract pose
            point_cloud = mesh[key]
            print("point_cloud: ", point_cloud)
            xyz = point_cloud.vertices
            print("pose shape: ", xyz.shape)
            print("pose: ", xyz)
            if point_cloud.colors is not None:
                colors = point_cloud.visual.vertex_colors
                print("colors shape: ", point_cloud.colors.shape)
                print("colors: ", colors)
            else:
                print("No colors")
            
def fetchPointcloud(path):
    cloud = trimesh.load(path, process=False)
    if isinstance(cloud, trimesh.PointCloud):
        # 점의 좌표(XYZ) 출력
        # print("Points (XYZ coordinates):\n", cloud.vertices)
        poses = cloud.vertices
        # 색상 정보 접근 및 출력
        if hasattr(cloud, 'colors') and cloud.colors is not None:
            # print("Colors (RGBA values):\n", cloud.colors)
            colors = cloud.colors
        else:
            print("No color data available.")
    else:
        print("Loaded data is not a point cloud.")
    
    return poses, colors
    
# import pygltf

# def load_glb_with_pygltf(path):
#     gltf = pygltf.GLTF2().load(path)
#     for mesh in gltf.meshes:
#         for primitive in mesh.primitives:
#             if 'COLOR_0' in primitive.attributes:
#                 colors = primitive.attributes['COLOR_0']
#                 print("Colors found:", colors)
#             if 'POSITION' in primitive.attributes:
#                 positions = primitive.attributes['POSITION']
#                 print("Positions found:", positions)





# print("Given path: ", given_path)
# fetchPly(given_path)
# print("Example path: ", example_path)
# fetchPly(example_path)
# load_glb_with_pygltf(example_path)
# fetchGlb(example_path)
fetchPointcloud(pointcloud_path)