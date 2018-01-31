from __future__ import print_function

import os
import shlex
import subprocess
from argparse import ArgumentParser
from common_utils.job_utils import generate_working_dir, delete_working_dir
from common_utils.s3_utils import upload_folder


def run_fastqc(working_dir, cmd_args, fastq_path):
    """
    Runs fastqc
   :param working_dir: Working directory
   :param cmd_args: Additional command-line arguments to pass in
   :param fastq_path: Local path to fastq file
   :return: Path to the result folder
    """
    # Prepare fastqc result path
    # fastqc_result_dir = os.path.join(working_dir, 'results/')
    fastqc_result_dir = os.path.join(working_dir, '')

    # Prepare fastqc log path
    fastqc_log_path = os.path.join(fastqc_result_dir, "log_fastqc.txt")

    # Prepare fastqc command
    cmd = "fastqc -o {0} {1} {2}".format(
        fastqc_result_dir, cmd_args, fastq_path)
    print(cmd)

    # Execute fastqc
    with open(fastqc_log_path, 'w') as log_file:
        subprocess.check_call(shlex.split(cmd), stdout=log_file)

    return fastqc_result_dir


def main():
    argparser = ArgumentParser()

    argparser.add_argument('--fastq_path', type=str,
                           help="fastq sequence file", required=True)
    argparser.add_argument('--working_dir', type=str, default="/scratch")
    argparser.add_argument('--cmd_args', type=str,
                           help="arguments/options for fastqc", default="")
    argparser.add_argument('--result_s3_path', type=str,
                           help="Result s3 path", required=True)

    args = argparser.parse_args()

    # Execute fastqc
    # working_dir = generate_working_dir(args.working_dir)

    print("Running fastqc")
    local_result_dir = run_fastqc(
        args.working_dir, args.cmd_args, args.fastq_path)

    print('Uploading {0} to {1}'.format(
        local_result_dir, args.result_s3_path))
    # upload_folder(args.result_s3_path, local_result_dir, False, True)

    # delete_working_dir(working_dir)
    print("Completed")


if __name__ == '__main__':
    main()
