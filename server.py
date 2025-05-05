import cv2
import socket
import pickle
import struct
import serial
from time import sleep
from threading import Thread
from gps import get_PVT

# creare video capture object for USB camera at /dev/video0
video_capture = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
video_capture.set(cv2.CAP_PROP_CONVERT_RGB, 0.0)

#gps_data global variable shared by read_gps and stream_video threads 
gps_data = tuple()


def stream_video():
	"""
	Create a server socket and listen for incoming connections.
	If a client socket is connected, stream video until client disconnects.
	Wait for a new client connection and repeat.
	"""
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
		server.bind(('raspberrypi.local', 9999))
		server.listen(10)
		
		while True:
			client, client_address = server.accept()
			print(f"{client_address} connected.")			
			with client:
				try:
					while True:
						"""
						Read frame from camera, combine with gps_data
						into a tuple, dump to a byte string and
						stream to the connected client.		
						"""
						ret, frame = video_capture.read()
						if ret:
							frame_data = pickle.dumps((frame, gps_data))
							size = struct.pack("L", len(frame_data))
							client.sendall(size + frame_data)
						
				except Exception as e:
					print(e)

	video_capture.release()
	
def read_gps():
	"""
		Read byte string from the GPS module connected to UART0 of the RaspberryPi.
		Extract GPRMC sentence from the byte string.
		Call get_PVT to return tuple of postion, velocity and time fields.
		Update the global variable gps_data.		
	"""
	serial_port = serial.Serial('/dev/ttyS0', 9600)
	while True:
		received_string = serial_port.read()
		sleep(0.5)	#GPS module updates every 1s, 0.5s is a suffient sampling time constant
		bytes_left_to_read = serial_port.inWaiting()
		received_string += serial_port.read(bytes_left_to_read)
		received_string = str(received_string)
		gprmc_sentence = received_string[received_string.find('$GPRMC'):received_string.find('\\r\\n')]
		if(gprmc_sentence):
			global gps_data
			gps_data = get_PVT(gprmc_sentence)
			#print(gps_data)
			
			
if __name__ == '__main__':
	"""
	Create two threads: one to stream_video and another to read_gps.
	setDaemon is disabled to allow threads run after main exit
	"""
	gps_thread = Thread(target=read_gps)
	gps_thread.start()
	stream_thread = Thread(target=stream_video)
	stream_thread.start()
	
			
