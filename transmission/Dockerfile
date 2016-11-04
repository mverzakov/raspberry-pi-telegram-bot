FROM hypriot/rpi-alpine-scratch

MAINTAINER Maxim Verzakov [maxim.verzakov@gmail.com]

RUN apk --no-cache --update add bash transmission-daemon \
    && rm -rf /var/cache/apk/*

ADD . .

RUN mkdir /etc/transmission-daemon \
    && cp conf/settings.json /etc/transmission-daemon/settings.json

EXPOSE 9091 51413/tcp 51413/udp

CMD sh docker-entrypoint.sh
