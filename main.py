import argparse
from datetime import datetime

import yaml
from apscheduler.schedulers.background import BlockingScheduler

from Objects.Config import Config
from Objects.GQLDevice import GQLDevice
from Objects.GraphQL import Connection
from Objects.GraphQL import Device


def main(cfgfile, savefile="dev_info.yaml") -> None:
    # Setup
    cfg = Config(cfg=cfgfile)
    dcheck(cfg=cfg, savefile=savefile)
    scheduler = BlockingScheduler()
    scheduler.add_job(
        dcheck, "interval", args=[cfg, savefile], minutes=cfg.interval, max_instances=1
    )
    scheduler.start()
    return


def dcheck(cfg: Config, savefile) -> str:
    try:
        with open(savefile) as f:
            dev_info: dict = yaml.load(f, Loader=yaml.BaseLoader)
    except FileNotFoundError:
        dev_info: dict = {}

    convert_null_to_none(dev_info)
    gc = Connection(cfg=cfg)
    convert_null_to_none(cfg)
    device_list = {}
    save_info = {}
    print(cfg)
    # Get List of SGQLC Devices from Voyance
    monitored_devices = gc.get_monitored_devices()
    # Make a list of Device Objects Merging in saved info from previous runs
    device: Device
    for device in monitored_devices:
        try:
            device_info = dev_info[device.uuid]
        except (KeyError, TypeError):
            print(f"{device.uuid} not found in {savefile}")
            device_info = None
        device_list[device.uuid] = GQLDevice(sgqlc_device=device, dev_info=device_info)

    # Iterate through Devices and check if they have been online recently, alert, then update the saved info
    device: GQLDevice
    for device_uuid, device in device_list.items():
        print(f"checking {device_uuid}")
        device.check_online(cfg=cfg)
        device.update_info(save_info=save_info)

    # Write Saved Info to File
    with open(savefile, "w") as f:
        yaml.dump(save_info, f, default_flow_style=False)

    return f"Completed run at {datetime.utcnow()}"


def convert_null_to_none(data) -> any:
    if isinstance(data, list):
        data[:] = [convert_null_to_none(i) for i in data]
    elif isinstance(data, dict):
        for k, v in data.items():
            data[k] = convert_null_to_none(v)
    return None if data == "null" else data


parser = argparse.ArgumentParser(
    description="Script to notify when a device from a list comes online."
)
parser.add_argument(
    "--cfgfile",
    required=True,
    help="Path to file where you want to pull the config from.",
)
parser.add_argument(
    "--savefile",
    default="dev_info.yaml",
    help="Path to file where you want to save info between runs.",
)
args = parser.parse_args()

main(cfgfile=args.cfgfile, savefile=args.savefile)
