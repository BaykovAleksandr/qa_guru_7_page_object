import os
from utils import util


def abs_path_from_project_root(relative_path):
    return os.path.join(util.ROOT_DIR, relative_path)