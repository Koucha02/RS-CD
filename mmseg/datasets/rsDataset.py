import os.path as osp
from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset

@DATASETS.register_module()
class rsDataset(BaseSegDataset):
    METAINFO = {
        'classes':['Invalid Annotation', 'Water', 'Transportation', 'Building',
                 'Farmland', 'Grassland', 'Forest', 'Soil', 'Other'],
        'palette':[[0, 0, 0], [255, 255, 255], [255, 0, 0], [0, 255, 0],
                   [0, 0, 255], [255, 255, 0], [128, 0, 128], [255, 165, 0],
                   [255, 192, 203]]
    }

    def __init__(self,
                 img_suffix='.tif',
                 seg_map_suffix='.png',
                 reduce_zero_label=False,
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            reduce_zero_label=reduce_zero_label,
            **kwargs)
