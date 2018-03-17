# Base image
FROM imamachi/bioconda2-debian9-slim-fastqc:latest

# Metadata
LABEL maintainer="Naoto Imamachi <naoto.imamachi@gmail.com>"
LABEL base.image="debian9-slim"
LABEL version="0.11.6"
LABEL software="fastqc_0.11.6"
LABEL software.version="20180131"
LABEL tags="NGS,Genomics,Transcriptomics,Bioconda,debian9-slim,fastqc"

# Application entry point
RUN conda update conda \
  && conda install fastqc=0.11.6 \
  && conda install -c conda-forge openjdk \
  && conda clean --all --yes
COPY ./fastqc/run_fastqc_local.py /run_fastqc_local.py

ENTRYPOINT ["python", "/run_fastqc_local.py"]