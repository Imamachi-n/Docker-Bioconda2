from __future__ import print_function

import os
import shlex
import subprocess
from argparse import ArgumentParser


def run_fastqc(fastq_path, cmd_args, working_dir):
    """
    Runs fastqc  
   :param fastq_path: Local path to fastq file  
   :param cmd_args: Additional command-line arguments to pass in  
   :param working_dir: Working directory  
   :return: Path to the result folder
    """
    # Prepare fastqc result path
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
    argparser.add_argument('--cmd_args', type=str,
                           help="arguments/options for fastqc", default="")
    argparser.add_argument('--working_dir', type=str, default="data/")

    args = argparser.parse_args()

    print("Creating working directory...")
    if not os.path.exists(args.working_dir):
        os.mkdir(args.working_dir)

    print("Running fastqc...")
    local_result_dir = run_fastqc(
        args.fastq_path, args.cmd_args, args.working_dir)

    print('Save the result in {0}.'.format(local_result_dir))

    print("successfully Completed !!")


if __name__ == '__main__':
    main()
