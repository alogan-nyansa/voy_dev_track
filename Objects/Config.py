import ast
from typing import List, Dict

import yaml
from pytz import timezone


class Config:
    def __init__(self, *, cfg) -> None:
        with open(cfg) as f:
            self.raw_cfg = yaml.load(f, Loader=yaml.BaseLoader)
        self.token = self.raw_cfg["token"]  # type: str
        self.endpoint = self.raw_cfg["endpoint"]  # type: str
        self.interval = int(self.raw_cfg["interval"])  # type: int
        self.timezone = timezone(self.raw_cfg["timezone"])  # type: timezone
        self.alerting = Alerting(alert_config=self.raw_cfg["alerting"])
        macs = {}
        for device in self.raw_cfg["macs"]:
            if isinstance(device, str):
                pieces = device.split()
                if len(pieces) > 1:
                    macs[pieces[0].upper()] = pieces[1]
                else:
                    macs[pieces[0].upper()] = "No Note Given"
            elif isinstance(device, dict):
                device_uuid, device_note = list(device.items())[0]
                macs[device_uuid.upper()] = device_note
        self.macs: Dict[str, str] = macs
        self.mac_list: List[str] = list(set(self.macs.keys()))

    def __repr__(self):
        data = self.__dict__.copy()
        data.pop("raw_cfg")
        return "{}({!r})".format(self.__class__.__name__, data)


class Alerting:
    def __init__(self, alert_config) -> None:
        self.constant = ast.literal_eval(
            alert_config["constant_alerting"]
        )  # type: bool
        self.alert_provider = alert_config["alert_provider"]  # type: str
        self.smtp_host = alert_config["smtp"]["host"]  # type: str
        self.smtp_port = int(alert_config["smtp"]["port"])  # type: int
        self.smtp_use_tls = ast.literal_eval(
            alert_config["smtp"]["use_tls"]
        )  # type: bool
        self.smtp_user = alert_config["smtp"]["user"]  # type: str
        self.smtp_pass = alert_config["smtp"]["pass"]  # type: str
        self.smtp_sender = alert_config["smtp"]["sender"]  # type: str
        self.smtp_receivers = alert_config["smtp"]["receivers"]  # type: List[str]

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)
