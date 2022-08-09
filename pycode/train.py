import sys, codecs
from tkinter import W
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
sys.dont_write_bytecode = True

from random import shuffle
from tqdm import tqdm
import matplotlib.pyplot as plt
import time
import datetime
import numpy as np
import random

import argparse
import subprocess
import datetime
import yaml
from shutil import copyfile
import os
import shutil
import __init__ as booger

import torch
from torchvision import models
import torch.nn as nn
import torch.nn.functional as nn_functional
import torch.optim as optim
import torch.backends.cudnn as cudnn

from tensorboardX import SummaryWriter

from models import vit
from common import dataset_mod
from common import make_datalist_mod
from common import data_transform_mod



if __name__ == "__main__":
    parser = argparse.ArgumentParser("train.py")

    parser.add_argument(
        '--train_cfg', '-c',
        type=str,
        required=False,
        default='../pyyaml/train_config.yaml',
        help='Training configuration file'
    )

    FLAGS, unparsed = parser.parse_known_args()

    print("Load YAML file")

    try:
        print("Opening train config file %s", FLAGS.train_cfg)
        CFG = yaml.safe_load(open(FLAGS.train_cfg, 'r'))
    except Exception as e:
        print(e)
        print("Error opening train config file %s", FLAGS.train_cfg)
        quit()

    save_top_path = CFG["save_top_path"]
    yaml_path = save_top_path + "/train_config.yaml"
    shutil.copy(FLAGS.train_cfg, yaml_path)

    pretrained_weights_top_directory = CFG["pretrained_weights_top_directory"]
    pretrained_weights_file_name = CFG["pretrained_weights_file_name"]
    pretrained_weights_path = os.path.join(pretrained_weights_top_directory, pretrained_weights_file_name)
    
    train_sequence = CFG["train"]
    valid_sequence = CFG["valid"]
    csv_name = CFG["csv_name"]
    index_csv_path = CFG["index_csv_path"]

    multiGPU = int(CFG["multiGPU"])

    img_size = int(CFG["hyperparameters"]["img_size"])
    patch_size = int(CFG["hyperparameters"]["patch_size"])
    num_classes = int(CFG["hyperparameters"]["num_classes"])
    num_frames = int(CFG["hyperparameters"]["num_frames"])
    attention_type = str(CFG["hyperparameters"]["attention_type"])
    depth = int(CFG["hyperparameters"]["depth"])
    num_heads = int(CFG["hyperparameters"]["num_heads"])
    deg_threshold = float(CFG["hyperparameters"]["deg_threshold"])
    batch_size = int(CFG["hyperparameters"]["batch_size"])
    num_epochs = int(CFG["hyperparameters"]["num_epochs"])
    optimizer_name = str(CFG["hyperparameters"]["optimizer_name"])
    lr = float(CFG["hyperparameters"]["lr"])
    alpha = float(CFG["hyperparameters"]["alpha"])
    num_workers = int(CFG["hyperparameters"]["num_workers"])
    save_step = int(CFG["hyperparameters"]["save_step"])
    mean_element = float(CFG["hyperparameters"]["mean_element"])
    std_element = float(CFG["hyperparameters"]["std_element"])

    print("Load Train Dataset")

    train_dataset = dataset_mod.ViViTAttitudeEstimatorDataset(
        data_list = make_datalist_mod.makeMultiDataList(train_sequence, csv_name),
        transform = data_transform_mod.DataTransform(
            img_size,
            mean_element,
            std_element
        ),
        phase = "train",
        index_dict_path = index_csv_path,
        dim_fc_out = num_classes,
        timesteps = num_frames,
        deg_threshold = deg_threshold,
        resize = img_size
    )

    print("Load Valid Dataset")

    valid_dataset = dataset_mod.ViViTAttitudeEstimatorDataset(
        data_list = make_datalist_mod.makeMultiDataList(valid_sequence, csv_name),
        transform = data_transform_mod.DataTransform(
            img_size,
            mean_element,
            std_element
        ),
        phase = "valid",
        index_dict_path = index_csv_path,
        dim_fc_out = num_classes,
        timesteps = num_frames,
        deg_threshold = deg_threshold,
        resize = img_size
    )

    print("Load Network")
    net = vit.TimeSformer(img_size, patch_size, num_classes, num_frames, depth, num_heads, attention_type, depth, num_heads, attention_type, pretrained_weights_path)
    print(net)