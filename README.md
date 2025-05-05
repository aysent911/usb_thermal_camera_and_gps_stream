# usb_thermal_camera_and_gps_stream
An application for streaming raw USB thermal camera frames and GPS data using RaspberryPi.  
Suitable for drone applications and remote monitoring/inspection applications.
## Requirements
1. RaspberryPi (tested on RaspberryPi Zero 2W)
2. USB Thermal Camera (tested on HT-203H 256*192)
3. GPS Module (tested with NEO-6M GPS Module) 
## Enable UART port on RaspberryPi
Refer [here](https://www.electronicwings.com/raspberry-pi/raspberry-pi-uart-communication-using-python-and-c) to enable UART port on RaspberryPi
## Install
1. Connect the USB thermal camera to USB port on the RaspberryPi
2. Connect the GPS module to the RaspberryPi as follows:
   ```
   GPS 5V  -> RaspberryPi 5V
   GPS GND -> GND
   GPS TX  -> GPIO15 (UART_RXD0)
   ```
3. Ensure the RaspberryPi and your PC are connected to the same local network.
4. ssh into the RaspberryPi
   ```
   ssh rasp@raspberrypi.local
   ```
6. Clone the repository
   ```
   git clone https://github.com/aysent911/usb_thermal_camera_and_gps_stream
   cd usb_thermal_camera_and_gps_stream
   ```
7. Install the streaming service
   ```
   sudo cp usb_thermal_camera.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable usb_thermal_camera
   sudo systemctl start usb_thermal_camera
   exit
   ```
8. clone and run the client script on the PC
    ```
    git clone https://github.com/aysent911/usb_thermal_camera_and_gps_stream
    cd usb_thermal_camera_and_gps_stream
    python3 client.py
    ``` 
