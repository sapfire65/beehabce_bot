## Собираем stable докер образ на основе python
#FROM python:3.12.0a4-alpine3.17
##FROM python:3.12-rc-alpine3.17
#
## update apk repositories
#RUN echo "https://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
#    echo "https://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories
#
## install chromedriver
#RUN apk update
#RUN apk add --no-cache chromium chromium-chromedriver tzdata
#
#
## Установка совместимой версии ChromeDriver
#RUN CHROME_VERSION=$(chromium-browser --version | grep -oP "(?<=Chromium )[0-9]+") && \
#    CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") && \
#    wget "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" && \
#    unzip chromedriver_linux64.zip && \
#    mv chromedriver /usr/bin/chromedriver && \
#    chmod +x /usr/bin/chromedriver && \
#    rm chromedriver_linux64.zip
#
#
## Вспомогательный набор библиотек
#RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
#RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk
#RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk
#
#
#WORKDIR /usr/workspace
#
## Copy the dependencies file to the working directory
#COPY ./requirements.txt /usr/workspace
#
## Install Python dependencies
#RUN pip3 install -r requirements.txt
#
#RUN pip list
#


# Собираем stable докер образ на основе python
FROM python:3.12.0a4-alpine3.17

# Установка зависимостей
RUN apk update && \
    apk add --no-cache chromium chromium-chromedriver tzdata && \
    apk add --no-cache udev ttf-freefont

# Установка необходимых библиотек
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk

# Установка совместимой версии ChromeDriver
RUN CHROME_VERSION=$(chromium --version | grep -oP "(?<=Chromium )[0-9]+") && \
    CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") && \
    wget "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip

WORKDIR /usr/workspace

# Копируем файл зависимостей в рабочий каталог
COPY ./requirements.txt /usr/workspace

# Установка зависимостей Python
RUN pip3 install -r requirements.txt

