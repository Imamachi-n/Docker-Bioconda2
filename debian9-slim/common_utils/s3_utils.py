from __future__ import print_function
import os
import subprocess
import shlex
import boto3


s3 = boto3.resource('s3')


def download_file(s3_path, directory_to_download, local=False):
    """
    Downloads an object from s3 to a local path
    :param s3_path: s3 object path
    :param directory_to_download: directory to download to
    :return: local file path of the object
    """
    # Local test - Copy a local folder to a current directory
    if local:
        cmd = 'docker cp'

    bucket = s3_path.split('/')[2]
    key = '/'.join(s3_path.split('/')[3:])

    object_name = key.split('/')[-1]

    local_file_name = os.path.join(directory_to_download, object_name)

    s3.Object(bucket, key).download_file(local_file_name)

    return local_file_name


def upload_folder(s3_path, local_folder_path, sse=True, local=False):
    """
    Uploads a local folder to S3
    Otherwise copy a local folder to local PC
    :param s3_path: s3 path to upload folder to
    :param local_folder_path: local folder path
    :param sse: boolean whether to enable server-side encryption
    """
    # Local test - Copy a local folder to a current directory
    if local:
        cmd = 'docker cp {0} {1}'.format(".", local_folder_path)
        subprocess.check_call(shlex.split(cmd))
        return

    cmd = 'aws s3 cp --recursive {0} {1}'.format(local_folder_path, s3_path)

    if sse:
        cmd += ' --sse'

    subprocess.check_call(shlex.split(cmd))
