from mmseg.apis import MMSegInferencer
# 将模型加载到内存中
inferencer = MMSegInferencer(model='checkpoints/unet_40000.pth')
# 推理
inferencer(r'E:\PycharmPrograms\seg-detection\mmsegmentation\dataset\train_with_seg\segmentation\img_dir\val\53.tif', show=True)
