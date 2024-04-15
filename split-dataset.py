import os
import random

# 目标文件夹路径
target_folder = './data/RSIPAC_CD/train/A'  # 请将 'your_target_folder' 替换成实际的文件夹路径

# 获取目标文件夹下所有文件名（不包含后缀）
file_names = [os.path.splitext(filename)[0] for filename in os.listdir(target_folder)]

# 打乱文件名列表的顺序
random.shuffle(file_names)

# 计算训练集和验证集的划分点
split_point = int(0.8 * len(file_names))  # 80% 用于训练，20% 用于验证

# 分割文件名列表
train_file_names = file_names[:split_point]
val_file_names = file_names[split_point:]

# 定义训练集和验证集文件的路径
train_file = os.path.join(os.path.dirname(target_folder), 'train.txt')
val_file = os.path.join(os.path.dirname(target_folder), 'val.txt')

# 将训练集文件名写入 train.txt
with open(train_file, 'w') as train_txt:
    train_txt.write('\n'.join(train_file_names))

# 将验证集文件名写入 val.txt
with open(val_file, 'w') as val_txt:
    val_txt.write('\n'.join(val_file_names))

print(f"已经成功生成 train.txt 和 val.txt 文件，共有 {len(train_file_names)} 个训练样本，{len(val_file_names)} 个验证样本。")
