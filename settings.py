import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

FA_FILE = os.environ.get("farsi_inptext_file")
EN_FILE = os.environ.get("english_intext_file")
IMAGEDIR = os.environ.get("input_imagedir_path")
FA_OUT_DIR = os.environ.get("farsi_output_folder")
EN_OUT_DIR = os.environ.get("english_output_folder")
IMAGE_OUT_DIR = os.environ.get("output_image_folder")
THRESH1 = os.environ.get("thresh_img1")
THRESH2 = os.environ.get("thresh_img2")
THRESH3 = os.environ.get("thresh_img3")
THRESH4 = os.environ.get("thresh_img4")
THRESH5 = os.environ.get("thresh_img5")

