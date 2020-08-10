"""
.. module:: src.handling_files_and_images.sysargv_python
   :synopsis: Read images using openCV that are passed as argument
"""

import click
from cv2 import imread, imshow, waitKey, destroyAllWindows


def read_image(image_path: str):
    return imread(image_path)


def show_image(image: imread):
    imshow("Image file", image)
    # Wait until key is pressed
    waitKey(0)
    destroyAllWindows()


def process(image_path: str):
    image = read_image(image_path)
    show_image(image)


@click.command()
@click.option(
    "--image_file", help="The path where the image file is found.",
)
def parse(image_file: str):
    process(image_file)


if __name__ == "__main__":
    parse()
