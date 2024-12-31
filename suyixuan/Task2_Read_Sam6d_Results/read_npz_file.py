"""
# Time： 2024/12/30 17:57
# Author： Yixuan Su
# File： read_npz_file.py
# IDE： PyCharm
# Motto：ABC(Never give up!)
# Description： TODO
"""

import numpy as np

# 加载 .npz 文件
file_path = '/Data/Example/outputs/sam6d_results/detection_ism.npz'  # 替换为你的文件路径
data = np.load(file_path)

# 查看文件中所有数组的名称
print("文件中的数组:", data.files)

# 查看文件中某个具体的数组内容
for array_name in data.files:
    print(f"{array_name}:")
    print(data[array_name])
