## CLARA Charge Front End CLI

### Building

```
pip install -r requirements.txt
pyinstaller chg_fe_cli.spec
.\dist\chg_fe_cli -h
```

### Usage
```
chg_fe_cli [-h] --ip IP [--sensitivity SENSITIVITY] [--calibration CALIBRATION] [--calibration_level CALIBRATION_LEVEL]

Command line interface for CLARA Charge Front ends

options:
  -h, --help            show this help message and exit
  --ip IP               IP address of the device.
  --sensitivity SENSITIVITY
                        Set the sensitivity of the device, 0 through 5 from most sensitive to least sensitive.
  --calibration CALIBRATION
                        Set the calibration state of the device, 0 or 1.
  --calibration_level CALIBRATION_LEVEL
                        Set the calibration level of the device, 0 through 255. Q_in = 2.048 * (calibration_level / 255)
```

