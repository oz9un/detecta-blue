# Author: Özgün Kültekin
# BLUETOOTH Scanner

import bluetooth, argparse, os

# GLOBAL VARIABLES:
SDPTOOL_BROWSE = False
SDPTOOL_RECORDS = False


def scanBluetooth(duration, iface):
    print("Scanning for bluetooth devices...\n")
    
    devices = bluetooth.discover_devices(duration=duration, lookup_names=True, lookup_class=True, device_id=iface)

    for b_addr, b_name, b_class in devices:
        print("==========================================")
        print("Device Name: ", b_name)
        print("Device Address: ", b_addr)
        print("Device Class: ", b_class)

        if SDPTOOL_BROWSE:
            print("-------USING SDPTOOL BROWSE FUNCTION-------")
            sdptoolBrowse(b_addr, b_name)
        if SDPTOOL_RECORDS:
            print("-------USING SDPTOOL RECORDS FUNCTION-------")
            sdptoolRecords(b_addr, b_name)
        if not SDPTOOL_RECORDS and not SDPTOOL_BROWSE:
            print("-------USING PYBLUEZ-------")
            checkServices(b_addr, b_name)

        print("==========================================")


def checkServices(b_addr, b_name):
    PYBLUEZ_SERVICES_OUTPUT = bluetooth.find_service(address=b_addr)

    if len(PYBLUEZ_SERVICES_OUTPUT) > 0:
        print("\n\n", len(PYBLUEZ_SERVICES_OUTPUT), "services found for ", b_name, ":")
        for service in PYBLUEZ_SERVICES_OUTPUT:
            print("--------------------------------")
            for key in service.keys():
                print(key, " -> ", service[key])
            print("--------------------------------\n")


def sdptoolBrowse(b_addr, b_name):
    print("\nSDPTOOL output for device ", b_name, ":")
    command = 'sdptool browse {addr}'.format(addr=b_addr)
    SDPTOOL_SERVICES_OUTPUT = os.popen(command).read()
    print("-------------------------------------")
    for row in SDPTOOL_SERVICES_OUTPUT.split('\n'):
        if row == '':
            print("-------------------------------------")
        print(row)

def sdptoolRecords(b_addr, b_name):
    print("\nSDPTOOL output for device ", b_name, ":")
    command = 'sdptool records {addr}'.format(addr=b_addr)
    SDPTOOL_SERVICES_OUTPUT = os.popen(command).read()
    print("-------------------------------------")
    for row in SDPTOOL_SERVICES_OUTPUT.split('\n'):
        if row == '':
            print("-------------------------------------")
        print(row)


if __name__ == '__main__':
    # Get user parameters:
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--scan_time", default=10, help="Scanning time for surrounding Bluetooth devices (seconds) (default=10)")
    parser.add_argument("-iface", "--interface", default=1, required=True, help="Set your bluetooth dongle iface (hciX). E.g: for hci1, type 1")
    parser.add_argument("-b", "--sdptool_browse", action='store_true', default=False, help="Use sdptool browse function instead of pybluez for discovering services")
    parser.add_argument("-r", "--sdptool_records", action='store_true', default=False, help="Use sdptool records function instead of pybluez for discovering services (more detailed but slower).")

    args = vars(parser.parse_args())

    if args['sdptool_browse']:
        SDPTOOL_BROWSE = True
    if args['sdptool_records']:
        SDPTOOL_RECORDS = True

    scanBluetooth(int(args['scan_time']), int(args['interface']))