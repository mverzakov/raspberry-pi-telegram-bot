FROM hypriot/rpi-alpine-scratch

MAINTAINER Maxim Verzakov [maxim.verzakov@gmail.com]

ENV base_dir /srv/telegram-bot

RUN apk --update add bash py-pip transmission-cli \
    && rm -rf /var/cache/apk/* \
    && mkdir -p $base_dir/requirements \
    && pip install --upgrade pip

WORKDIR ${base_dir}

ADD . $base_dir

RUN pip install -r requirements/base.txt \
    && rm -rf /root/.cache/pip/ \
    && cp ./config/supervisord.conf /etc/supervisord.conf

CMD sh docker-entrypoint.sh
