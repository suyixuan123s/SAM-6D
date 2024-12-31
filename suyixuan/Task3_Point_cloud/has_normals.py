"""
# Time： 2024/12/30 17:57
# Author： Yixuan Su
# File： has_normals.py
# IDE： PyCharm
# Motto：ABC(Never give up!)
# Description： TODO
"""
import open3d as o3d

# 加载点云文件
point_cloud = o3d.io.read_point_cloud(
    r"G:\AI\Pose_Estimation\SAM-6D\Data\Example\obj_000005.ply")

# 检查点云是否包含法线
if point_cloud.has_normals():
    print("点云包含法线")
else:
    print("点云不包含法线")
