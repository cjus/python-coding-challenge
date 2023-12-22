FROM ubuntu:22.04
LABEL maintainer="Carlos Justiniano cjus@ieee.org"

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y iputils-ping curl git vim unzip && \
    apt-get install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get install python3.10 -y && \
    apt-get install -y python3-pip python3-dev python3-graphviz

#RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install

WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install numpy nltk ipykernel juniper lxml autopep8
RUN python3 -m nltk.downloader popular
RUN pip3 install openai transformers
RUN pip3 install --upgrade openai transformers

CMD tail -f /dev/null
