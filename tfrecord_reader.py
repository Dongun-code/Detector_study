import os.path as op
import json
import tensorflow as tf
import cv2
from tensorflow.python.ops.gen_random_ops import random_shuffle

import settings
from config import Config as cfg
import utils.util_function as uf

class TfrecordReader:
    def __init__(self, tfrpath, shuflle=False, batch_size = cfg.Train.BATCH_SIZE, epochs=1):
        self.tfrpath = tfrpath
        self.shuffle = random_shuffle
        self.batch_size = batch_size
        self.epochs = epochs
        self.config = self.read_tfrecord_config(tfrpath)
        self.feature_dict = self.get_features(self.config)