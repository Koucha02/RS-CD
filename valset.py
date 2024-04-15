import os
import shutil

# 目标文件夹路径
target_folder = './data/RSIPAC_CD/train/label'  # 请将 'your_target_folder' 替换成实际的文件夹路径

# 读取val.txt中的文件名
val_file = os.path.join(os.path.dirname(target_folder), 'val.txt')

with open(val_file, 'r') as file:
    val_file_names = file.read().splitlines()

# 创建valA文件夹
valA_folder = os.path.join(os.path.dirname(target_folder), 'vallabel')
os.makedirs(valA_folder, exist_ok=True)

# 遍历val.txt中的文件名，将同名文件剪切到valA文件夹
for file_name in val_file_names:
    source_file = os.path.join(target_folder, file_name + '.png')  # 请将 '.ext' 替换为实际的文件扩展名
    destination_file = os.path.join(valA_folder, file_name + '.png')

    if os.path.exists(source_file):
        shutil.move(source_file, destination_file)

print(f"已经成功将文件剪切到 val 文件夹中。")
