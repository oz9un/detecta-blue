
# DETECTA-BLUE 🔎


Detecta-blue scans surrounding Bluetooth devices and checks
their detailed service information with using **sdptool** and **pybluez**.

## Arguments

Detecta-blue currently has 5 arguments:

1. **-t (--scan_time):** Scanning time for surrounding BLE devices (seconds) (default=10).
2. **-iface (--interface):** Bluetooth dongle iface (hciX). Type 1 for hci1.
3. **-b (--sdptool_browse):** Use sdptool's *browse* function instead of *pybluez* for detecting services.
4. **-r (--sdptool_records):** Use sdptool's *records* function instead of *pybluez* for detecting services.
## Usage Examples


#### Example 1:
- Use hci1 bluetooh interface.
- Scan nearby Bluetooth devices for 15 seconds.
- Use pybluez library for detecting services.
```python
└─$ sudo python3 detecta_blue.py -i 1 -t 15
```

#### Example 2: 
- Use hci0 bluetooh interface.
- Scan nearby Bluetooth devices for 10 seconds (default).
- Use sdptool's records function for detecting services.
```python
└─$ sudo python3 detecta_blue.py -i 0 -r
```

#### Example 3: 
- Use hci1 bluetooh interface.
- Scan nearby Bluetooth devices for 20 seconds.
- Use sdptool's records function for detecting services.
- Use sdptool's browse function for detecting services.
```python
└─$ sudo python3 detecta_blue.py -i 1 -t 20 -r -b
```




  
## Help Menu

![Help Menu](https://i.ibb.co/C6fGNzc/detecta-blue-helpmenu.png)