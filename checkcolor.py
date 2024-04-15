import cv2
import numpy as np
import matplotlib.pyplot as plt


def parse_label_value(label_value):
    # 将三位数的标签值解析为一级和二级类别
    first_category = label_value // 100
    second_category = label_value % 100
    return first_category, second_category


def visualize_label(label_image):
    # 可视化标签图像
    plt.imshow(label_image, cmap='jet')
    plt.colorbar()
    plt.title("Label Image")
    plt.show()


def main():
    input_label_path = r"E:\PycharmPrograms\seg-detection\mmsegmentation\dataset\CD\train\label\1.png"

    label_image = cv2.imread(input_label_path, cv2.IMREAD_UNCHANGED)

    print("Label Image Shape:", label_image.shape)
    print("Label Image Value:", label_image)

    visualize_label(label_image)

    while True:
        x = int(input("Enter x-coordinate: "))
        y = int(input("Enter y-coordinate: "))

        if 0 <= x < label_image.shape[1] and 0 <= y < label_image.shape[0]:
            label_value = label_image[y, x]
            first_category, second_category = parse_label_value(label_value)
            print(f"Clicked position: ({x}, {y}), Label Value: {label_value}")
            print(f"First Category: {first_category}, Second Category: {second_category}")
        else:
            print("Coordinates are out of bounds.")


if __name__ == "__main__":
    main()
