import sys
import tensorflow as tf
import numpy as np

def print_progress(status_msg):
    #   Note the \r which means the line should overwrite itself.
    msg = "\r" + status_msg
    #Print it.
    sys.stdout.write(msg)
    sys.sstdout.flush()

def to_float_image(im_tensor):
    return tf.image.convert_image_dtype(im_tensor, dtype=tf.float32) * 2 - 1
    