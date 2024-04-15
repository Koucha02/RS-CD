import matplotlib.pyplot as plt
import numpy
from PIL import Image
import numpy as np

def count_and_list_unique_colors(image_path):
    try:
        image = Image.open(image_path)
        pixels = image.getdata()
        unique_colors = set(pixels)
        num_unique_colors = len(unique_colors)

        print(f"图片中有 {num_unique_colors} 种不同的像素颜色：")
        for color in unique_colors:
            print(color)

        return num_unique_colors
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
#     image_path = r"E:\PycharmPrograms\seg_mine\mmsegmentation\dataset\train_with_seg\segmentation\train\ann_dir\train\0.png"  # 请将"your_image.png"替换为你的图片路径
#     num_colors = count_and_list_unique_colors(image_path)
#     if num_colors is not None:
#         print(f"图片中共有 {num_colors} 种不同的像素颜色。")
    # 读取PNG图像
    image_path = r"E:\MobaDownload\ori\test_2.png" # 替换成实际的PNG图像路径
    image = Image.open(image_path)
    # 将图像转换为NumPy数组
    image_array = np.array(image)
    # 将1映射为255
    image_array[image_array == 1] = 255
    # 创建新的图像对象
    new_image = Image.fromarray(image_array)
    # 保存新的PNG图像
    plt.imshow(new_image)
    plt.show()




