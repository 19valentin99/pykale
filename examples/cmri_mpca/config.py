"""
Default configurations for cardiac MRI data (ShefPAH) processing and classification
"""

from yacs.config import CfgNode as CN

# -----------------------------------------------------------------------------
# Config definition
# -----------------------------------------------------------------------------

_C = CN()

# -----------------------------------------------------------------------------
# Dataset
# -----------------------------------------------------------------------------
_C.DATASET = CN()
_C.DATASET.SOURCE = "https://github.com/pykale/data/raw/main/images/ShefPAH-179/SA_64x64.zip"
_C.DATASET.ROOT = "../data"
_C.DATASET.IMG_DIR = "DICOM"
_C.DATASET.BASE_DIR = "SA_64x64"
_C.DATASET.FILE_FORAMT = "zip"
_C.DATASET.LANDMARK_FILE = "landmarks.csv"
_C.DATASET.MASK_DIR = "Mask"
# ---------------------------------------------------------------------------- #
# Image processing
# ---------------------------------------------------------------------------- #
_C.PROC = CN()
_C.PROC.SCALE = 2

# ---------------------------------------------------------------------------- #
# Machine learning pipeline
# ---------------------------------------------------------------------------- #
_C.PIPELINE = CN()
_C.PIPELINE.CLASSIFIER = "linear_svc"  # ["svc", "linear_svc", "lr"]

# ---------------------------------------------------------------------------- #
# Misc options
# ---------------------------------------------------------------------------- #
_C.OUTPUT = CN()
_C.OUTPUT.ROOT = "./outputs"  # output_dir


def get_cfg_defaults():
    return _C.clone()
