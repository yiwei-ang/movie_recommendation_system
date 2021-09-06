FROM ubuntu:latest
ENV PROJECT_DIR=/usr/src/app/movie_recommendation_system/
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt-get update \
    && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN mkdir -p ${PROJECT_DIR}
ADD environment.yml /root

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh
RUN conda --version
RUN conda config --set ssl_verify False
RUN conda env update -f /root/environment.yml

ENV PYTHONPATH=${PROJECT_DIR}:$PYTHONPATH

WORKDIR ${PROJECT_DIR}
EXPOSE 8888
CMD ["jupyter", "lab", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]