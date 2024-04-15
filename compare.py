from PIL import Image
import os
import numpy as np

# 定义标签颜色和分割结果颜色
green_color = (0, 255, 0)  # 绿色
red_color = (255, 0, 0)    # 红色

# 设置输入文件夹路径
label_folder = r'E:\PycharmPrograms\seg-detection\mmsegmentation\dataset\LEVIR-CD\test\label'  # 包含标签文件的文件夹路径
segmentation_folder = r'E:\MobaDownload\fcn'  # 包含分割结果文件的文件夹路径
# 设置输出文件夹路径
output_folder = './compare-results/fcn/'  # 输出差异图像的文件夹路径

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历两个文件夹中的图像文件
label_files = os.listdir(label_folder)
segmentation_files = os.listdir(segmentation_folder)

for label_file in label_files:
    if label_file.endswith('.png'):
        # 构造标签文件和分割结果文件的完整路径
        label_path = os.path.join(label_folder, label_file)
        segmentation_file = label_file  # 假设分割结果文件与标签文件同名
        segmentation_path = os.path.join(segmentation_folder, segmentation_file)

        # 打开图像文件
        label_img = Image.open(label_path)
        segmentation_img = Image.open(segmentation_path)

        # 将标签图像转换为NumPy数组
        label_array = np.array(label_img)

        # 将分割结果图像转换为NumPy数组并提取其中一个通道
        segmentation_array = np.array(segmentation_img)[:, :, 0]  # 提取第一个通道（红色通道）

        # 创建一个差异图像，初始化为全黑
        diff_img = Image.new('RGB', label_img.size, (0, 0, 0))
        diff_array = np.array(diff_img)

        # 比较两个图像并将差异部分标为绿色或红色
        diff_array[np.logical_and(label_array == 255, segmentation_array == 0)] = (0, 255, 0)  # 绿色
        diff_array[np.logical_and(label_array == 0, segmentation_array == 255)] = (255, 0, 0)  # 红色

        # 保存差异图像
        diff_img = Image.fromarray(diff_array)
        output_file = os.path.join(output_folder, label_file)
        diff_img.save(output_file)

print("差异图像已保存到", output_folder)



