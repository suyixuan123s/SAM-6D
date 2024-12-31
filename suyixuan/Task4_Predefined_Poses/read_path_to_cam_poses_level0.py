"""
# Time： 2024/12/30 17:57
# Author： Yixuan Su
# File： read_path_to_cam_poses_level0.py
# IDE： PyCharm
# Motto：ABC(Never give up!)
# Description： TODO
"""
import numpy as np

# 加载 .npy 文件
cam_poses = np.load(
    r'G:\AI\Pose_Estimation\SAM-6D\SAM-6D\Instance_Segmentation_Model\utils\poses\predefined_poses\obj_poses_level0.npy')

# 打印出文件的维度和内容
print("cam_poses shape:", cam_poses.shape)
print("First camera pose matrix:\n", cam_poses[0])

# 如果想查看所有的相机位姿矩阵
for idx, pose in enumerate(cam_poses):
    print(f"Camera Pose {idx}:\n", pose)
