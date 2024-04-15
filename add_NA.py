import os
import cv2
import numpy as np

def add_white_noise(image, variance=25):
    row, col, ch = image.shape
    sigma = np.sqrt(variance)
    gauss = np.random.normal(0, sigma, (row, col, ch))
    noisy = image + gauss
    noisy = np.clip(noisy, 0, 255)
    return noisy.astype(np.uint8)

def add_speckle_noise(image, intensity=0.1):
    """
    在图像中添加散斑噪声

    参数:
    - image: 输入的图像
    - intensity: 噪声强度，范围在0到1之间，值越大噪声越强

    返回:
    - 添加散斑噪声后的图像
    """
    h, w, _ = image.shape
    noise = np.random.normal(loc=0, scale=intensity, size=(h, w, 3))
    speckled_image = image + image * noise
    speckled_image = np.clip(speckled_image, 0, 255).astype(np.uint8)
    return speckled_image

def add_striped_noise(image, intensity=0.02):
    h, w, _ = image.shape
    num_stripes = int(h * intensity)
    # 生成条纹噪声
    noise = np.random.randint(0, 256, size=(num_stripes, w, 3), dtype=np.uint8)
    # 随机选择要添加噪声的位置
    positions = np.random.randint(0, h, size=num_stripes)
    # 将条纹噪声叠加到图像上
    image[positions, :, :] = noise
    return image

def apply_noise_to_folder(input_folder, output_folder, noise_type='white', intensity=0.2):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.tif', '.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_folder, filename)
            original_image = cv2.imread(image_path)

            if noise_type == 'white':
                noisy_image = add_white_noise(original_image, variance=intensity)
            elif noise_type == 'speckle':
                noisy_image = add_speckle_noise(original_image, intensity=intensity)
            elif noise_type == 'striping':
                noisy_image = add_striped_noise(original_image, intensity=intensity)
            else:
                print("Invalid noise type. Supported types: 'white', 'speckle', 'striping'")
                return

            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, noisy_image)

# 使用示例
input_folder_path = "./data/LEVIR-CD/val/B"
output_folder_path = "./data/NAnoise/speckle_test/B"

# apply_noise_to_folder(input_folder_path, output_folder_path, noise_type='white', intensity=81)
apply_noise_to_folder(input_folder_path, output_folder_path, noise_type='speckle', intensity=0.2)
# apply_noise_to_folder(input_folder_path, output_folder_path, noise_type='striping', intensity=0.2)
