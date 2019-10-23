import pprint
from time import sleep

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from Objects.Config import Config
from Objects.vapi2_schema import vapi2_schema as schema

pp = pprint.PrettyPrinter()


class Connection:
    def __init__(self, *, cfg: Config):
        self.cfg = cfg
        self.token = cfg.token
        self.url = cfg.endpoint
        self.ep = HTTPEndpoint(self.url, {'api-token': self.token})
        return

    def get_location_list(self, verbose=False):
        page = 1
        end_page = 2
        ll = {}

        while end_page >= page:
            op = Operation(schema.NyansaGraphQLQuery)
            lc = op.location_list(page=page, page_size=500)
            lc.page()
            lc.page_count()
            lc.locations.id()
            lc.locations.name()
            data = self.ep(op)
            print(op)
            locs = (op + data).location_list
            for loc in locs.locations:
                ll[loc.name] = loc.id
            end_page = locs.page_count
            page += 1
            sleep(2)
        if verbose:
            pp.pprint(ll)
        return ll

    def get_device_att_hist(self, uuids=None, to_date=None, from_date=None):
        dev_list = []
        op = Operation(schema.NyansaGraphQLQuery)
        atthist = op.device_list(uuids=uuids)
        # ftime = parse(from_date)
        # ttime = parse(to_date)
        atthist.devices()
        atthist.devices.uuid()
        # atthist.devices.attribute_changes(attribute_names=['apMacAddr'], from_date=ftime, to_date=ttime)
        atthist.devices.attribute_changes.sample_time()
        atthist.devices.attribute_changes.new_value()
        atthist.devices.attribute_changes.old_value()
        atthist.devices.attribute_changes.related_entity()
        atthist.devices.attribute_changes.related_entity.description()
        # pp.pprint(op)
        data = self.ep(op)
        devinfo = (op + data).device_list
        for d in devinfo.devices:
            dev_list.append(d)
        return dev_list

    def get_all_clients(self) -> list:
        dev_list = []
        page = 1
        end_page = 2
        while end_page >= page:
            op = Operation(schema.NyansaGraphQLQuery)
            dev = op.device_list(uuids=self.cfg.macs, page=page, page_size=500, sort_by=['uuid'])
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
            for d in devinfo.devices:
                dev_list.append(d)
            end_page = devinfo.page_count
            print(f'Run {page} of {end_page} - Length {len(dev_list)}')
            page += 1
            sleep(.5)
        return dev_list
