from PIL import Image

def overlay_images(input_folder1, input_folder2, output_folder):
    # 获取文件夹中的图片列表
    images1 = os.listdir(input_folder1)
    images2 = os.listdir(input_folder2)

    for img_name1 in images1:
        if img_name1 in images2:
            img_path1 = os.path.join(input_folder1, img_name1)
            img_path2 = os.path.join(input_folder2, img_name1)
            img1 = Image.open(img_path1)
            img2 = Image.open(img_path2)

            # 将两个图片转换为RGBA模式，以便处理透明通道
            img1 = img1.convert('RGBA')
            img2 = img2.convert('RGBA')

            # 获取图片的像素数据
            pixels1 = img1.load()
            pixels2 = img2.load()

            width, height = img1.size

            for x in range(width):
                for y in range(height):
                    color1 = pixels1[x, y]
                    color2 = pixels2[x, y]

                    # 如果任一像素是红色或绿色，则保持红色或绿色
                    if color1 == (255, 0, 0, 255) or color2 == (255, 0, 0, 255):
                        pixels1[x, y] = (255, 0, 0, 255)  # 红色
                    elif color1 == (0, 255, 0, 255) or color2 == (0, 255, 0, 255):
                        pixels1[x, y] = (0, 255, 0, 255)  # 绿色
                    else:
                        # 根据颜色优先级选择要保留的颜色
                        color_priority = [(255, 255, 255, 255), (0, 0, 0, 255)]
                        for color in color_priority:
                            if color1 == color:
                                pixels1[x, y] = color1
                                break
                            elif color2 == color:
                                pixels1[x, y] = color2
                                break

            # 保存叠加后的图片
            img1.save(os.path.join(output_folder, img_name1), 'PNG')

if __name__ == "__main__":
    import os

    input_folder1 = r"E:\MobaDownload\fcn/"  # 第一个文件夹的路径
    input_folder2 = r"E:\PycharmPrograms\seg-detection\mmsegmentation\compare-results\fcn/"  # 第二个文件夹的路径
    output_folder = r"./coloroutput/fcn/"   # 输出文件夹的路径

    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    overlay_images(input_folder1, input_folder2, output_folder)
