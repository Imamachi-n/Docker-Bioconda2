# Base image
FROM imamachi/docker-bioconda2-debian9-slim:latest

# Metadata
LABEL maintainer="Naoto Imamachi <naoto.imamachi@gmail.com>"
LABEL base.image="debian9-slim"
LABEL version="1"
LABEL software="fastqc0.11.6"
LABEL software.version="01122018"
LABEL tags="NGS,Genomics,Transcriptomics,Bioconda,debian9-slim,fastqc"

# Install Miniconda2 & Bioconda
RUN conda install fastqc=0.11.6
