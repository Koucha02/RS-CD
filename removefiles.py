import os

def delete_files_with_suffix(path):
    if not os.path.exists(path):
        print(f"Error: The specified path '{path}' does not exist.")
        return

    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)

        # Check if it's a file (not a directory) and contains "_n"
        if os.path.isfile(file_path) and "_n" in file_name:
            # Delete the file
            os.remove(file_path)
            print(f"Deleted: {file_name}")

if __name__ == "__main__":
    user_path = r'data/LEVIR-CD/val/label/'
    delete_files_with_suffix(user_path)
