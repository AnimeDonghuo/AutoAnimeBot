FROM python:3.10.4-slim-buster

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

RUN apt-get -qq update && apt-get -qq install -y git wget pv jq python3-dev mediainfo gcc aria2 libsm6 libxext6 libfontconfig1 libxrender1 libgl1-mesa-glx ffmpeg

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["bash", "run.sh"]
