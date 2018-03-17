#!/bin/bash
LOCAL_WORKING_DIR="/Users/imamachinaoto/Desktop/NGS/data"
DOCKER_WORKING_DIR="/data"
DOCKER_IMAGE="fastqc-aws-debian9-slim-bioconda2:0.11.6.local"
FASTQ_FILE="RefSeq_hg38_2015-08-19_NM_ultraSlim.fq"

docker run --rm -it \
-v ${LOCAL_WORKING_DIR}:${DOCKER_WORKING_DIR} \
${DOCKER_IMAGE} \
--fastq_path ${DOCKER_WORKING_DIR}/${FASTQ_FILE} \
--working_dir ${DOCKER_WORKING_DIR}
