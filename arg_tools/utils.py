# AUTOGENERATED! DO NOT EDIT! File to edit: 00_utils.ipynb (unless otherwise specified).

__all__ = ['gdown_unzip', 'pose_dis', 'waypoint']

# Cell

import os
import sys
import gdown
import copy
import math
from zipfile import ZipFile

def gdown_unzip(id, filename):
    """download a zipfile and unzip it under data directory
    """
    dataset_url = 'https://drive.google.com/u/1/uc?id=' + id
    dataset_name = "data/" + filename

    if not os.path.isdir(dataset_name):
        gdown.download(dataset_url, output = dataset_name + '.zip', quiet=False)
        zip_file = ZipFile( dataset_name + '.zip')
        #zip_file.extractall()
        zip_file.extractall("data/") # depends on how to zip it
        zip_file.close()


def pose_dis(pose_1, pose_2):
    """Compute distance between pose_1 and pose_2
    """
    x = pose_1.target_pose.position.x - pose_2.target_pose.position.x
    y = pose_1.target_pose.position.y - pose_2.target_pose.position.y
    z = pose_1.target_pose.position.z - pose_2.target_pose.position.z

    dis = math.sqrt(x**2+y**2+z**2)

    return dis

def waypoint(current_pose, Target_pose):
    """Generate a list of way points from current pose to target pose

    Input : current pose, target pose
    Return : a list of way points

    """
    waypoint_list = []
    factor = 0.5
    sub_pose = current_pose.copy()

    # threshold : distance between sub_pose and target_pose = 0.05 meter
    while pose_dis(current_pose, target_pose) > 0.05:
        sub_pose.target_pose.position.x = (sub_pose.target_pose.position.x + Target_pose.target_pose.position.x)*factor
        sub_pose.target_pose.position.y = (sub_pose.target_pose.position.y + Target_pose.target_pose.position.y)*factor
        sub_pose.target_pose.position.z = (sub_pose.target_pose.position.z + Target_pose.target_pose.position.z)*factor

        waypoint_list.append(sub_pose.copy())

    waypoint_list.append(Target_pose)

    return waypoint_list