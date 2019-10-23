from typing import List

import yaml
from pytz import timezone


class Config:
    def __init__(self, *, cfg):
        with open(cfg) as f:
            self.raw_cfg = yaml.load(f, Loader=yaml.BaseLoader)
        self.token = self.raw_cfg['token']  # type: str
        self.endpoint = self.raw_cfg['endpoint']  # type: str
        self.interval = int(self.raw_cfg['interval'])  # type: int
        self.macs = self.raw_cfg['macs']  # type: List[str]
        self.timezone = timezone(self.raw_cfg['timezone'])  # type: timezone
        self.alerting = Alerting(alert_config=self.raw_cfg['alerting'])
        return

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)


class Alerting:
    def __init__(self, alert_config):
        self.constant = alert_config['constant_alerting']  # type: bool
        self.alert_provider = alert_config['alert_provider']  # type: str
        self.smtp_host = alert_config['smtp']['host']  # type: str
        self.smtp_port = int(alert_config['smtp']['port'])  # type: int
        self.smtp_user = alert_config['smtp']['user']  # type: str
        self.smtp_pass = alert_config['smtp']['pass']  # type: str
        self.smtp_sender = alert_config['smtp']['sender']  # type: str
        self.smtp_receivers = alert_config['smtp']['receivers']  # type: List[str]
        return

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)
