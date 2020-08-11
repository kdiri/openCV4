"""
.. module:: src.handling_files_and_images.write_images
   :synopsis: Write images using openCV
"""

from src.handling_files_and_images.read_images
from cv2 import imread

images_path = "images/image_file.png"

def write_image_to_file(image: imread):
    cv2.imwrite(images_path, image)


