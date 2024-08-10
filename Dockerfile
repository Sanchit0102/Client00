FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3-pip git \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip

WORKDIR /Spotify-Downloader
RUN chmod 777 /Spotify-Downloader
RUN apt update && apt upgrade -y && apt install gcc ffmpeg python3 python3-pip -y
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "-m", "mbot"]
