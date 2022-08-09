FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu20.04


########## nvidia-docker1 hooks ##########
LABEL com.nvidia.volumes.needed="nvidia_driver"
ENV PATH /usr/local/nvidia/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}
########## non-interactive ##########
ENV DEBIAN_FRONTEND=noninteractive



RUN apt-get update && apt-get install -y \
	vim \
	wget \
	unzip \
	git \
	build-essential \
	libsm6 \
	libxrender1 \
	libxext-dev

RUN apt-get update && \
	apt-get install -y \
	python3-pip \
	python3-tk

RUN python3 -m pip install -U --force-reinstall pip

RUN pip3 install torch \
                torchvision \
                torchvideo \
                'git+https://github.com/facebookresearch/fvcore' \
                simplejson \
                einops \
                timm \
                psutil \
                scikit-learn \
                opencv-python \
                tensorboard \
                torchsummary \
                tqdm \
                matplotlib \
                pyyaml \
                ttach \
                grad-cam \
                tensorboardX

RUN mkdir /home/pycode && \
    mkdir /home/log && \
    mkdir -p /home/log/train_log && \
    mkdir -p /home/log/inference_test_log && \
    mkdir -p /home/log/other_test_log && \
    cd /home/pycode && \
    git clone https://github.com/Hibiki1020/attitude_estimator_in_timesformer.git && \
    cd attitude_estimator_in_timesformer && \
    python3 setup.py build develop

RUN cd /home

WORKDIR /home
