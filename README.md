# usb_thermal_camera_and_gps_stream
An application for streaming raw USB thermal camera frames and GPS data using RaspberryPi
## Enable UART port on RaspberryPi
Refer [here](https://www.electronicwings.com/raspberry-pi/raspberry-pi-uart-communication-using-python-and-c) to enable UART port on RaspberryPi
## Install
1. Connect the USB thermal camera to USB port on the RaspberryPi
2. Connect the GPS module to the RaspberryPi as follows:
   GPS 5V  -> RaspberryPi 5V
   GPS GND -> GND
   GPS TX  -> GPIO15 (UART_RXD0)
4. Ensure the RaspberryPi and your PC are coonected to the same local network.
5. ssh into the RaspberryPi
   ```ssh rasp@raspberrypi.local```
7. Clone the repository
   ```
   git clone https://github.com/aysent911/usb_thermal_camera_and_gps_stream
   cd usb_thermal_camera_and_gps_stream
   ```
9. Install the streaming service
   ```
   sudo cp usb_thermal_camera.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable usb_thermal_camera
   sudo systemctl start usb_thermal_camera
   exit
   ```
10. clone and run the client script on the PC
    ```
    git clone https://github.com/aysent911/usb_thermal_camera_and_gps_stream
    cd usb_thermal_camera_and_gps_stream
    python3 client.py
    ``` 
