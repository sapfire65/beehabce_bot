# Собираем stable докер образ на основе python
FROM python:3.12.0a4-alpine3.17
#FROM python:3.12-rc-alpine3.17

# update apk repositories
RUN echo "https://dl-cdn.alpinelinux.org/alpine/v3.17/main" >> /etc/apk/repositories; \
    echo "https://dl-cdn.alpinelinux.org/alpine/v3.17/community" >> /etc/apk/repositories


# Вспомогательный набор библиотек
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk



# install chromedriver
RUN apk update &&  \
    apk upgrade && \
    apk add --no-cache chromium chromium-chromedriver


WORKDIR /usr/workspace

# Copy the dependencies file
COPY ./requirements.txt /usr/workspace

# install Python dependencies
RUN pip3 install -r requirements.txt

