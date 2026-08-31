# Dockerfile for Tissue Simulation Toolkit 2.0
# Requires docker, ssh access to github and X11 forwarding to run the GUI
# Created during the TST-MD hackaton 22+23 May 2025 in Leiden
# If you have questions contact Zoë Lange

FROM debian:buster

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
        openssh-client \
        vim \
        git \
        pkg-config \
        curl \
        cmake \
        build-essential \
        qt5-default \
        qttools5-dev-tools \
        qttools5-dev \
        qtbase5-dev \
        qtbase5-dev-tools \
        qt5-qmake \
        qtchooser \
        libglu1-mesa-dev \
        libgl1-mesa-dev \
        libx11-xcb1 \
        libxrender1 \
        libxcb1 \
        libxcb-glx0 \
        libxcb-keysyms1 \
        libxcb-image0 \
        libxcb-shm0 \
        libxcb-icccm4 \
        libxcb-sync1 \
        libxcb-xfixes0 \
        libxcb-shape0 \
        libxcb-randr0 \
        libxcb-render-util0 \
        libxext6 \
        libxkbcommon-x11-0 \
        libxi6 \
        libxtst6 \
        x11-xserver-utils \
        gcc \
        g++ \
        binutils \
        make \
        zlib1g-dev \
        libpng-dev \
        ocl-icd-opencl-dev \
        libqt5opengl5-dev \
        wget \
        libssl-dev libbz2-dev \
        libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev \
        xz-utils tk-dev libffi-dev liblzma-dev python-openssl ninja-build \
        libeigen3-dev

RUN curl https://pyenv.run | bash

ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"
        
RUN pyenv install 3.10.13 && pyenv global 3.10.13
        
RUN mkdir -p /home/mduser

RUN git clone --recursive -b TST2.0 \
        https://github.com/sbr-shakibi/Tissue-Simulation-Toolkit.git \
        /home/mduser/Tissue-Simulation-Toolkit \
    && cd /home/mduser/Tissue-Simulation-Toolkit

WORKDIR /home/mduser/Tissue-Simulation-Toolkit/
RUN make

RUN make HOOMD_CORES=4 with_adhesions
USER mduser