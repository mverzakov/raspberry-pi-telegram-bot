FROM alpine:latest

MAINTAINER Maxim Verzakov [maxim.verzakov@gmail.com]

RUN apk --no-cache --update add bash transmission-daemon \
    && rm -rf /var/cache/apk/*

ADD . .

EXPOSE 9091 51413/tcp 51413/udp

CMD sh docker-entrypoint.sh