#!/bin/bash
docker run -it -v /Users/imamachinaoto/Desktop/NGS/:/data \
fastqc-aws-debian9-slim-bioconda2:0.11.6 \
--fastq_path data/RefSeq_hg38_2015-08-19_NM_slim.fq \
--working_dir data \
--result_s3_path tests