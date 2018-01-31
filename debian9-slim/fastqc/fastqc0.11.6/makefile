NAME=fastqc-aws-debian9-slim-bioconda2
TAG=0.11.6
UNDERSCORE_TAG=0_11_6

all: build push

build:
		docker build -t $(NAME):$(TAG) -t $(NAME):latest -f Dockerfile --build-arg VERSION=$(TAG) --build-arg UNDERSCORE_VERSION=$(UNDERSCORE_TAG) ../..

push:
		docker push $(NAME):$(TAG)
		docker push $(NAME):latest

start:
		docker run -it $(NAME):$(TAG)

rm:
		docker rm `docker ps -aq`

rmi:
		docker rmi $(NAME):$(TAG) $(NAME):latest