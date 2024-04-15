from PIL import Image
import os

def check_image_dimensions(path):
    if not os.path.exists(path):
        print(f"Error: The specified path '{path}' does not exist.")
        return

    # Get a list of image files in the specified path
    image_files = [file for file in os.listdir(path) if file.lower().endswith(('.tif','.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    if not image_files:
        print("No image files found in the specified path.")
        return

    # Get the dimensions of the first image
    first_image_path = os.path.join(path, image_files[0])
    with Image.open(first_image_path) as reference_image:
        reference_dimensions = reference_image.size

    # Check dimensions of other images
    for image_file in image_files[1:]:
        image_path = os.path.join(path, image_file)
        with Image.open(image_path) as image:
            if image.size != reference_dimensions:
                print(f"Image dimensions mismatch: {image_file} ({image.size}) differs from the reference image ({reference_dimensions})")

if __name__ == "__main__":
    user_path = r'data/LEVIR-CD/val/label/'
    check_image_dimensions(user_path)
