import socket
import subprocess 

UDP_IP = "0.0.0.0"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    if data.decode() == "connect":
        print("Connecting to Bluetooth device...")
        subprocess.call([r'C:\your destination folder path\connect.bat'])
        print("Connectied!")

    elif data.decode() == "disconnect":
        print("Disconnecting to Bluetooth device...")
        subprocess.call([r'C:\your destination folder path\disconnect.bat'])
        print("Disconnectied!")
