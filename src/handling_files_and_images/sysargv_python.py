"""
.. module:: src.handling_files_and_images.sysargv_python
   :synopsis: Basic python parameter parser
"""
import logging
import sys

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info(f"The name of the script being processed is {sys.argv[0]}")
    logging.info(f"The number of arguments of the script: {len(sys.argv)}")
    logging.info(f"The arguments of the script are {sys.argv}")
