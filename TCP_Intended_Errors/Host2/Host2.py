import socket
from os import listdir

soket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #SOCK_STREAM is TCP, SOCK_DGRAM is UDP

HOST = "localhost"
PORT2 = 8500
buf = 1024
bFileFound = 0
clientA = False
temp = ""

soket.bind((HOST,PORT2))


print("Ready to recieve file...")
while True:

    sData = soket.recv(buf)
    fDownloadFile = open("burak", "wb")
    try:
        while sData:
            fDownloadFile.write(sData)
            sData,server = soket.recvfrom(buf)
            soket.settimeout(2)

            print("Downloading from Server...")
        print("Download Completed")
    except Exception:
        print("Error happened!")
    break


soket.close()