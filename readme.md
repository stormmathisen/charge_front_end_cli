## CLARA Charge Front End CLI

### Building

```
pip install -r requirements.txt
pyinstaller chg_fe_cli.spec
.\dist\chg_fe_cli -h
```

### Usage
```
chg_fe_cli [-h] [-s SENSITIVITY] [-c CALIBRATION] [-l CALIBRATION_LEVEL] [-v] ip

Command line interface for CLARA Charge Front ends

positional arguments:
  ip                    IP address of the device.

options:
  -h, --help            show this help message and exit
  -s SENSITIVITY, --sensitivity SENSITIVITY
                        Set the sensitivity of the device, 0 through 5 from most sensitive to least sensitive.
  -c CALIBRATION, --calibration CALIBRATION
                        Set the calibration state of the device, 0 or 1.
  -l CALIBRATION_LEVEL, --calibration_level CALIBRATION_LEVEL
                        Set the calibration level of the device, 0 through 255. Q_in [pC] = 2.048 * 66 * (calibration_level / 255)
  -v, --verbose
  ```

#### Example
This will set the highest senstivitiy, with the calibration input enabled, inputting 10.6 pC of charge.
```
chg_fe_cli -s 0 -c 1 -l 20 192.168.93.14
```
