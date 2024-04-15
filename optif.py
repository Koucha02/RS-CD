import tifffile
import matplotlib.pyplot as plt
import torch
def optif(file_path, channel):
    try:
        with tifffile.TiffFile(file_path) as tif:
            img = tif.asarray() 
            img = img[channel-1:channel, :, :]
            print(f"shape: {img.shape}")

            plt.imshow(img.transpose(1, 2, 0))
            plt.title('tif')
            plt.show()

    except Exception as e:
        print(f"err: {e}")

tif_path = r'E:\PycharmPrograms\seg-detection\open-cd\city_001_VNI_2012051114.tif'
optif(tif_path, channel=33)
