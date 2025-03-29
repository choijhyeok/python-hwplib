FROM ubuntu:20.04

RUN apt-get update && apt-get install -y locales && \
    locale-gen ko_KR.UTF-8 && \
    update-locale LANG=ko_KR.UTF-8

ENV DEBIAN_FRONTEND=noninteractive \
    JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \
    LANG=ko_KR.UTF-8 \
    LANGUAGE=ko_KR.UTF-8 \
    LC_ALL=ko_KR.UTF-8
ENV PATH="${JAVA_HOME}/bin:${PATH}"

RUN apt-get install -y \
    wget \
    git \
    python3 \
    python3-pip \
    openjdk-8-jdk \
    fonts-nanum* \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install flask requests JPype1==1.4.1


WORKDIR /app

COPY . /app/python-hwplib

WORKDIR /app/python-hwplib

EXPOSE 7860

CMD ["python3", "hwp_flask.py"]
