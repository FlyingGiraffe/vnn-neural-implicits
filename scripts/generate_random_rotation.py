import os
import logging
import torch
from pytorch3d.transforms import random_rotation
import numpy as np

''' Initialization of the the 3D shape dataset.

Args:
    dataset_folder (str): dataset folder
    split (str): which split is used
    categories (list): list of categories to use
    no_except (bool): no exception
    transform (callable): transformation applied to data points
'''
# Attributes
dataset_folder = 'data/ShapeNet'
rotation_folder = 'data_rotations/ShapeNet'

categories = os.listdir(dataset_folder)
categories = [c for c in categories
              if os.path.isdir(os.path.join(dataset_folder, c))]

# Get all models
for c in categories:
    category_path = os.path.join(dataset_folder, c)
    models = os.listdir(category_path)
    models = [m for m in models
              if os.path.isdir(os.path.join(category_path, m))]
    for m in models:
        rotation_path = os.path.join(rotation_folder, c, m)
        os.makedirs(rotation_path)
        
        rotation_file = os.path.join(rotation_path, 'random_rotations.npz')
        rot_so3 = random_rotation().numpy()
        rot_z = np.random.rand() * 360
        rot = {'so3': rot_so3, 'z': rot_z}
        np.savez(rotation_file, **rot)
        