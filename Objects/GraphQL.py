from time import sleep
from typing import List

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from Objects.Config import Config
from Objects.vapi2_schema import Device
from Objects.vapi2_schema import vapi2_schema as schema


class Connection:
    def __init__(self, *, cfg: Config):
        self.cfg = cfg
        self.token = cfg.token
        self.url = cfg.endpoint
        self.ep = HTTPEndpoint(self.url, {"api-token": self.token})

    def get_monitored_devices(self) -> List[Device]:
        dev_list = []
        page = 1
        end_page = 2
        while end_page >= page:
            op = Operation(schema.NyansaGraphQLQuery)
            dev = op.device_list(
                uuids=self.cfg.mac_list, page=page, page_size=500, sort_by=["uuid"]
            )
            dev.page()
            dev.page_count()
            dev.devices()
            dev.devices.uuid()
            dev.devices.ip_address()
            dev.devices.hostname()
            dev.devices.ap_name()
            dev.devices.ap_mac_addr()
            dev.devices.essid()
            dev.devices.snr_db()
            dev.devices.last_updated()
            dev.devices.voyance_url()
            data = self.ep(op)
            devinfo = (op + data).device_list
            for d in devinfo.devices:  # type: Device
                dev_list.append(d)
            end_page = devinfo.page_count
            print(f"Run {page} of {end_page} - Length {len(dev_list)}")
            page += 1
            sleep(0.5)
        return dev_list
