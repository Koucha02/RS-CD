import os
import shutil
#改代码用于把train中的文件按照val.txt选择的放进val文件夹里
# 定义文件路径
root_dir = './dataset/train_with_seg/segmentation/train/'
# 分别修改type为ann_dir和img_dir
type = 'ann_dir/'
img_dir = os.path.join(root_dir, type)
val_txt_path = os.path.join(root_dir, 'val.txt')
val_img_dir = os.path.join(root_dir, type)+'val/'

# 创建存放val图像的目录
if not os.path.exists(val_img_dir):
    os.makedirs(val_img_dir)

# 读取val.txt中的文件名（不带后缀）
with open(val_txt_path, 'r') as file:
    val_filenames = [line.strip() for line in file.readlines()]

# 遍历train目录中的文件
for filename in os.listdir(img_dir):
    if filename.split('.')[0] in val_filenames:
        src_path = os.path.join(img_dir, filename)
        dst_path = os.path.join(val_img_dir, filename)
        shutil.move(src_path, dst_path)
        print(f"Moved {filename} to val directory.")
