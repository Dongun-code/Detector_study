import os
import os.path as op
import tensorflow as tf
import numpy as np
import json
import copy
from glob import glob
import shutil
from timeit import default_timer as timer

import utils.util_class as uc
import utils.util_function as uf
from tfrecord.example_maker import ExampleMaker
import tfrecord.tfr_util as tu

def drive_manager_factory(dataset_name, split, srcpath):
    if dataset_name == "kitti":
        from tfrecord.readers.kitti_reader import KittiDriveManager
        return KittiDriveManager(srcpath, split)
    else:
        assert 0, f"[drive_manager_factory] invalid dataset name: {dataset_name}"

def drive_reader_factory(dataset_cfg, split, drive_path):
    if dataset_cfg.NAME == "kitti":
        from tfrecord.readers.kitti_reader import KittiReader
        return KittiReader(drvie_path, split, dataset_cfg)
    else:
        assert 0, f"[drive_reader_factory] invalid dataset name: {dataset_cfg.NAME}"