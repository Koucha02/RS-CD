import os

def rename_mp3_to_wav(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".mp3"):
            mp3_file = os.path.join(input_folder, file_name)
            wav_file = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".wav")
            os.rename(mp3_file, wav_file)

if __name__ == "__main__":
    input_folder = r"./hui"
    output_folder = r"./huiwav"

    rename_mp3_to_wav(input_folder, output_folder)
