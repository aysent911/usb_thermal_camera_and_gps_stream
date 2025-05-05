import cv2
import socket
import pickle
import struct

# Create client socket and connect to server at raspberrypi.local:9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('raspberrypi.local', 9999))

received_byte_string = b""
size = struct.calcsize("L")

while True:
	# Unpack received byte string size 
	while len(received_byte_string) < size:
		received_byte_string += client.recv(4096)

	frame_size_byte_string = received_byte_string[:size]
	frame_size = struct.unpack("L", frame_size_byte_string)[0]
	
	frame_data_byte_string = received_byte_string[size:]
	

	# Unpack frame data byte string
	while len(frame_data_byte_string) < frame_size:
		frame_data_byte_string += client.recv(4096)

	frame_data = frame_data_byte_string[:frame_size]
	received_byte_string = frame_data_byte_string[frame_size:]

	# load frame data
	frame_data = pickle.loads(frame_data)
	frame = frame_data[0]
	gps_data = frame_data[1]

	# Convert the raw image to RGB
	rgb_frame = cv2.cvtColor(frame,  cv2.COLOR_YUV2BGR_YUYV)
	
	#add gps datetime and gps coordinates to image array
	cv2.putText(rgb_frame, gps_data[1]+' '+gps_data[2], (10, 20),\
	cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
	
	cv2.putText(rgb_frame, gps_data[3]+','+gps_data[4], (10, 40),\
	cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
	
	cv2.imshow('Video', rgb_frame)

	#quit
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

client.close()
cv2.destroyAllWindows()
