# Собираем stable докер образ на основе python
FROM python:3.12.0a4-alpine3.17
#FROM python:3.12-rc-alpine3.17

# update apk repositories
RUN echo "https://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
    echo "https://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories

RUN apk add --no-cache tzdata

# install chromedriver
RUN apk update
RUN apk add --no-cache chromium chromium-chromedriver tzdata



# Установка зависимостей
RUN apk update && \
    apk add --no-cache curl jq chromium chromium-chromedriver tzdata && \
    apk add --no-cache udev ttf-freefont

# Установка совместимой версии ChromeDriver
RUN CHROME_VERSION="91" && \
    CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") && \
    wget "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip

# Установка Chrome
RUN CHROME_URL=$(curl -s https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json | jq -r '.channels.Stable.downloads.chrome[] | select(.platform == "linux64") | .url') && \
    curl -sSLf --retry 3 --output /tmp/chrome-linux64.zip "$CHROME_URL" && \
    unzip /tmp/chrome-linux64.zip -d /opt && \
    ln -s /opt/chrome-linux64/chrome /usr/local/bin/chrome && \
    rm /tmp/chrome-linux64.zip






# Вспомогательный набор библиотек
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk


WORKDIR /usr/workspace

# Copy the dependencies file to the working directory
COPY ./requirements.txt /usr/workspace

# Install Python dependencies
RUN pip3 install -r requirements.txt

RUN pip list



