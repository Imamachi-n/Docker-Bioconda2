from __future__ import print_function
import os
import shutil
import uuid
from datetime import datetime


def generate_working_dir(working_dir_base):
    """
    Creates a unique working directory to combat job multitenancy
    :param working_dir_base: base working directory
    :return: a unique subfolder in working_dir_base with a uuid
    """

    working_dir = os.path.join(working_dir_base, str(uuid.uuid4()))
    try:
        os.mkdir(working_dir)
    except Exception as e:
        return working_dir_base
    return working_dir


def generate_working_dir_local(working_dir_base):
    """
    Creates a unique working directory on local PC.
    :param working_dir_base: base working directory
    :return: a unique subfolder in working_dir_base with a uuid
    """

    working_dir = os.path.join(
        working_dir_base, datetime.now().strftime("%Y%m%d%H%M%S"))
    try:
        os.mkdir(working_dir)
    except Exception as e:
        return working_dir_base
    return working_dir


def delete_working_dir(working_dir):
    """
    Deletes working directory
    :param working_dir: working directory
    """

    try:
        shutil.rmtree(working_dir)
    except Exception as e:
        print('Cannot delete {0}'.format(working_dir))
