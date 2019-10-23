import argparse
from datetime import datetime

import yaml

from Objects.Config import Config
from Objects.GQLDevice import GQLDevice
from Objects.GraphQL import Connection
from Objects.GraphQL import Device


def main(cfgfile, savefile='dev_info.yaml') -> str:
    # Setup
    cfg = Config(cfg=cfgfile)
    try:
        with open(savefile) as f:
            dev_info = yaml.load(f, Loader=yaml.BaseLoader)
    except FileNotFoundError:
        dev_info = {}
    convert_null_to_none(dev_info)
    gc = Connection(cfg=cfg)
    dl = {}
    save_info = {}

    # Get List of SGQLC Devices from Voyance
    cl = gc.get_all_clients()

    # Make a list of Device Objects Merging in saved info from previous runs
    for d in cl:  # type: Device
        try:
            d_info = dev_info[d.uuid]
        except (KeyError, TypeError):
            print(f'not found {d}')
            d_info = None
        dl[d.uuid] = GQLDevice(sgqlc_device=d, dev_info=d_info)

    # Iterate through Devices and check if they have been online recently, alert, then update the saved info
    for did, d in dl.items():  # type: str, GQLDevice
        print(f'checking {did}')
        d.check_online(cfg=cfg)
        d.update_info(save_info=save_info)

    # Write Saved Info to File
    with open(savefile, 'w') as f:
        yaml.dump(save_info, f, default_flow_style=False)

    return f'Completed run at {datetime.utcnow()}'


def convert_null_to_none(data) -> any:
    if isinstance(data, list):
        data[:] = [convert_null_to_none(i) for i in data]
    elif isinstance(data, dict):
        for k, v in data.items():
            data[k] = convert_null_to_none(v)
    return None if data == 'null' else data


parser = argparse.ArgumentParser(description='Script to notify when a device from a list comes online.')
parser.add_argument("--cfgfile", required=True, help="Path to file where you want to pull the config from.")
parser.add_argument("--savefile", default='dev_info.yaml', help="Path to file where you want to save info between runs.")
args = parser.parse_args()

main(cfgfile=args.cfgfile, savefile=args.savefile)
