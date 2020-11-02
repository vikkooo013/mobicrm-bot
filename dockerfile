FROM python:3.7-slim
SHELL ["/bin/bash", "-c"]
# default to utf-8 file encoding
ENV LANG C.UTF-8
ARG GITHUB_TOKEN
RUN apt-get update -qq &&\
    apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    openssh-client \
    graphviz-dev \
    pkg-config \
    git-core \
    openssl \
    libssl-dev \
    libffi6 \
    libffi-dev \
    libpng-dev \
    curl && \
    apt-get clean && \
    rm -rf /var/lib/apt-get/lists/*/tmp/*var/tmp/* && \
    mkdir /app
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5055 5002
RUN python3 -m rasa train
CMD ["/bin/bash", "-c", "./start_service.sh"]