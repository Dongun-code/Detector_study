import os.path as op
import numpy as np
from glob import glob
import cv2
from tfrecord.readers.reader_base import DatasetReaderBase, DriveManagerBase




class KittiReader(DatasetReaderBase):
    def __init__(self, drive_path, split, dataset_cfg):
        super().init(drive_path, split, dataset_cfg)

    """
    public method used outside this class
    """

    def init_drive(self, drive_path, split):
        frame_names = glob(op.join(drive_path, "*.png"))
        frame_names.sort()
        if split == "train":
            frame_names = frame_names[:-500]
        else:
            frame_names = frame_names[-500:]
        print("")



