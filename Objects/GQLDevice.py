import smtplib
import ssl
from datetime import datetime, timedelta, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dateutil import parser

from Objects.Config import Config
from Objects.vapi2_schema import Device


class GQLDevice:
    def __init__(self, sgqlc_device: Device, dev_info: dict) -> None:
        self.uuid = sgqlc_device.uuid  # type: str
        self.ip_address = sgqlc_device.ip_address  # type: str
        self.hostname = sgqlc_device.hostname  # type: str
        self.ap_name = sgqlc_device.ap_name  # type: str
        self.ap_mac_addr = sgqlc_device.ap_mac_addr  # type: str
        self.essid = sgqlc_device.essid  # type: str
        self.snr_db = sgqlc_device.snr_db  # type: int
        self.last_updated = sgqlc_device.last_updated  # type: datetime
        self.voyance_url = sgqlc_device.voyance_url  # type: str
        if dev_info is None:
            self.last_run = datetime.now(timezone.utc) - timedelta(days=2)
            self.last_ap = None
            self.last_alert = datetime.now(timezone.utc) - timedelta(days=2)
        else:
            self.last_run = parser.parse(dev_info['last_run'])
            self.last_ap = dev_info['last_ap']
            self.last_alert = parser.parse(dev_info['last_alert'])

    def __repr__(self) -> str:
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)

    def check_online(self, cfg: Config) -> None:
        # Records are updated every 5 minutes, so use 2 * 5 minutes or 2 * interval, whichever is greater
        if cfg.interval < 5:
            time_delta = timedelta(minutes=10)
        else:
            time_delta = timedelta(minutes=2 * cfg.interval)
        '''
        Check if device has been on recently, 
        then check if we have alerted in the last day or if we are configured to alert on every AP change and it has changed APs
        Call alert if True
        '''
        '''
        Debug Code, yes I know there is probably a better way to do this
        print(f'time - delta: {(datetime.now(timezone.utc) - time_delta)}')
        print(f'last_updated: {self.last_updated}')
        print(f'last AP: {self.last_ap}')
        print(f'current AP: {self.ap_mac_addr}')
        print(f'equal AP: {self.last_ap != self.ap_mac_addr}')
        '''
        if (datetime.now(timezone.utc) - time_delta) < self.last_updated:
            if (cfg.alerting.constant and self.last_ap != self.ap_mac_addr) or (datetime.now(timezone.utc) - self.last_alert > timedelta(hours=24)):
                self.alert(cfg=cfg)
        return

    def update_info(self, save_info: dict) -> None:
        save_info.setdefault(self.uuid, {})['last_run'] = datetime.now(timezone.utc).isoformat()
        save_info.setdefault(self.uuid, {})['last_ap'] = self.ap_mac_addr
        save_info.setdefault(self.uuid, {})['last_alert'] = self.last_alert.isoformat()
        return

    def alert(self, cfg: Config) -> None:
        if cfg.alerting.alert_provider == 'smtp':
            self.smtp_alert(cfg=cfg)
        self.last_alert = datetime.now(timezone.utc)
        return

    def smtp_alert(self, cfg: Config) -> None:
        fmt = '%Y-%m-%d %H:%M %Z'
        msg = MIMEMultipart()
        msg['From'] = cfg.alerting.smtp_sender
        msg['To'] = ', '.join(cfg.alerting.smtp_receivers)
        msg['Subject'] = f'Subject: Tracked Device Online - {self.uuid} on AP: {self.ap_name} at {self.last_updated.astimezone(cfg.timezone).strftime(fmt)}'
        msg.attach(MIMEText(f'''
            Tracked device:
                MAC: {self.uuid}
                Hostname: {self.hostname}
                IP: {self.ip_address}
                SSID: {self.essid}
                Last AP Name: {self.ap_name}
                Last AP MAC: {self.ap_mac_addr}
                Last SNR: {self.snr_db}
                Last Updated: {self.last_updated.astimezone(cfg.timezone).strftime(fmt)}
                Link to Voyance: {self.voyance_url}
            ''', 'plain'))
        print(msg)
        if cfg.alerting.smtp_use_tls:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(cfg.alerting.smtp_host, cfg.alerting.smtp_port, context=context) as server:
                server.login(user=cfg.alerting.smtp_user, password=cfg.alerting.smtp_pass)
                server.send_message(msg)
                server.quit()
        else:
            with smtplib.SMTP(cfg.alerting.smtp_host, cfg.alerting.smtp_port) as server:
                server.send_message(msg)
                server.quit()
        return
