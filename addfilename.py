import os


def rename_files_with_suffix(path):
    if not os.path.exists(path):
        print(f"Error: The specified path '{path}' does not exist.")
        return

    for file_name in os.listdir(path):
        old_file_path = os.path.join(path, file_name)

        # Check if it's a file (not a directory)
        if os.path.isfile(old_file_path):
            base_name, extension = os.path.splitext(file_name)
            new_file_name = f"{base_name}_n{extension}"
            new_file_path = os.path.join(path, new_file_name)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {file_name} -> {new_file_name}")


if __name__ == "__main__":
    user_path = r"E:\PycharmPrograms\seg-detection\open-cd\data\LEVIR-CD\test\label"
    rename_files_with_suffix(user_path)
