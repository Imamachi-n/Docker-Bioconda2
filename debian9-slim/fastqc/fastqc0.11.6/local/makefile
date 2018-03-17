NAME=fastqc-aws-debian9-slim-bioconda2
TAG=0.11.6.local
UNDERSCORE_TAG=0_11_6_local

all: build push

build:
		docker build -t $(NAME):$(TAG) -t $(NAME):latest -f Dockerfile ../../..

build-no-cache:
		docker build --no-cache -t $(NAME):$(TAG) -t $(NAME):latest -f Dockerfile ../../..

push:
		docker push $(NAME):$(TAG)
		docker push $(NAME):latest

start:
		docker run -it --rm $(NAME):$(TAG)

rm:
		docker rm `docker ps -aq`

rmi:
		docker rmi $(NAME):$(TAG) $(NAME):latest