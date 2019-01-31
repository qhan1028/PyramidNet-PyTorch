FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04
MAINTAINER qhan@ailabs.tw

# basic packages
ENV TZ=Asia/Taipei

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
		\
        python3-pip \
        \
        git \
        wget \
        curl \
        vim \
		htop \
		tree \
		\
        ca-certificates \
        sudo \
        fonts-liberation \
        zsh \
        \
        locales \
        tzdata\
        apt-utils \
        \
 && locale-gen en_US.UTF-8 \
 && echo $TZ | tee /etc/timezone \
 && dpkg-reconfigure --frontend noninteractive tzdata

ENV LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

# copy project files
COPY . /app
WORKDIR /app

# install python packages
RUN python3 -m pip install --upgrade pip \
 && python3 -m pip install -r requirements.txt

CMD ["sleep", "infinity"]
