_base_ = [
    # '../_base_/models/fcn_unet_s5-d16.py', '../_base_/datasets/chase_db1.py',
    # '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
    'E:\PycharmPrograms\seg_mine\mmsegmentation\configs\_base_\models\\fcn_unet_s5-d16.py',
    'E:\PycharmPrograms\seg_mine\mmsegmentation\configs\_base_\datasets\\rsDataset.py',
    'E:\PycharmPrograms\seg_mine\mmsegmentation\configs\_base_\default_runtime.py',
    'E:\PycharmPrograms\seg_mine\mmsegmentation\configs\_base_\schedules\schedule_40k.py'
]
crop_size = (512, 512)
data_preprocessor = dict(size=crop_size)
model = dict(
    data_preprocessor=data_preprocessor,
    test_cfg=dict(crop_size=(128, 128), stride=(85, 85)))
