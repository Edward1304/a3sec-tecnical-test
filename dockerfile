FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential

WORKDIR /app
ADD . /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . /app

ADD . /app

CMD ["python3", "app.py"]

