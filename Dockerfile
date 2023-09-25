FROM python:3.12.0a4-alpine3.17

RUN echo "https://dl-cdn.alpinelinux.org/alpine/v3.17/main" >> /etc/apk/repositories; \
    echo "https://dl-cdn.alpinelinux.org/alpine/v3.17/community" >> /etc/apk/repositories

RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk

COPY  requirements.txt /app/

RUN apk update &&  \
    apk upgrade && \
    apk add --no-cache chromium chromium-chromedriver

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt


RUN pip list

