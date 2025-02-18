from settings import Settings
import argparse
import socket
import json

'''
Arguments:
    --sensitivity: 0 through 5
    --calibration: 0 or 1
    --calibration_level: 0 through 255
    Default is 0, 0, 0
'''

def main():
    # Parse arguments
    settings = Settings()
    parser = argparse.ArgumentParser(prog="chg_fe_cli", description='Command line interface for CLARA Charge Front ends')
    parser.add_argument('ip', type=str, help='IP address of the device.')
    parser.add_argument('-s', '--sensitivity', type=int, default=0, help=f'Set the sensitivity of the device, 0 through 5 from most sensitive to least sensitive.')
    parser.add_argument('-c', '--calibration', type=int, default=0, help='Set the calibration state of the device, 0 or 1.')
    parser.add_argument('-l', '--calibration_level', type=int, default=0, help='Set the calibration level of the device, 0 through 255. Q_in [pC] = 2.048 * 66 * (calibration_level / 255)')
    parser.add_argument('-v', '--verbose',
                    action='store_true')
    args = parser.parse_args()

    settings.set_calibration_reference("REF2048mV")

    # Set the sensitivity
    if args.sensitivity >= 0 and args.sensitivity < 6:
        if args.sensitivity == 0:
            settings.set_integrator("FB0")
        elif args.sensitivity == 1:
            settings.set_integrator("FB1")
        elif args.sensitivity == 2:
            settings.set_integrator("FB2")
        elif args.sensitivity == 3:
            settings.set_integrator("FB3")
        elif args.sensitivity == 4:
            settings.set_integrator("FB4")
        elif args.sensitivity == 5:
            settings.set_integrator("FB5")
    else:
        print("Invalid sensitivity value. Must be between 0 and 5.")

    # Set the calibration state
    if args.calibration == 0:
        settings.set_io_input("EXT")
    elif args.calibration == 1:
        settings.set_io_input("CAL")
    else:
        print("Invalid calibration value. Must be 0 or 1.")

    # Set the calibration level
    if args.calibration_level >= 0 and args.calibration_level < 256:
        settings.set_calibration_level(args.calibration_level)
    else:
        print("Invalid calibration level. Must be between 0 and 255.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        s.connect((args.ip, 56000))
        s.sendall(settings.to_json().encode())
        s.settimeout(10)
        if args.verbose:
            print("Settings sent")
            print(json.dumps(settings.settings, indent=4))
        return(0)
    
if __name__ == '__main__':
    main()