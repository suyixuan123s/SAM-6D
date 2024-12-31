"""
# Time： 2024/12/30 17:57
# Author： Yixuan Su
# File： read_json_file.py
# IDE： PyCharm
# Motto：ABC(Never give up!)
# Description： TODO
"""
import json

# 定义读取JSON文件的函数
def read_json_file(file_path):
    try:
        # 打开文件并加载JSON内容
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)  # 加载JSON数据
        return data
    except FileNotFoundError:
        return f"文件 {file_path} 未找到。"
    except json.JSONDecodeError:
        return "文件不是有效的JSON格式。"
    except IOError:
        return "读取文件时发生错误。"

# 文件路径
file_path = r"G:\AI\Pose_Estimation\SAM-6D\Data\Example\outputs\sam6d_results\detection_ism.json"

# 调用函数读取文件内容
json_data = read_json_file(file_path)

# 输出文件内容
print(json_data)


