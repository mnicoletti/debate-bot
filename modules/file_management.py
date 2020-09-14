import os
import logging

log = logging.getLogger(__name__)

def create_dir(dir_path) -> bool:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        return True
    return False