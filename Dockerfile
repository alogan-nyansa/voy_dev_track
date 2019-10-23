FROM python:3.7.5-alpine3.10

ENV VERSION 0.9.1
ENV VOLUME ["/config"]
RUN mkdir -p /voy_dev_track \
    && mkdir -p /config \
    && mkdir -p /voy_dev_track/tmp \
    && wget https://github.com/alogan-nyansa/voy_dev_track/archive/$VERSION.tar.gz -P /voy_dev_track/tmp \
    && tar xvzf /voy_dev_track/tmp/$VERSION.tar.gz -C /voy_dev_track/tmp/ \
    && cp -R /voy_dev_track/tmp/voy_dev_track-$VERSION/* /voy_dev_track/ \
    && rm -r /voy_dev_track/tmp/ \
    && [ ! -f "/config/config_sample.yaml" ] && cp /voy_dev_track/config_sample.yaml /config \
    && [ ! -f "/config/dev_info.yaml" ] && touch /config/dev_info.yaml  \
    && pip install -r /voy_dev_track/requirements.txt
CMD ["python", "/voy_dev_track/main.py", "--cfgfile", "/config/config.yaml", "--savefile", "/config/dev_info.yaml"]

