from socket import *
from os import listdir
import os
import time
start_time = time.time()

sunucuAd = 'localhost'
sunucuPort = 12346
buf = 1024

sunucuSocket = socket(AF_INET, SOCK_DGRAM)

sunucuSocket.bind((sunucuAd,sunucuPort))
print ('Client B Veri almaya hazırdır')
try:
    while True:
        sData = "Temp"

        sData, istemciAdres = sunucuSocket.recvfrom(buf)
        fDownloadFile = open("burak", "wb")

        while sData:
            fDownloadFile.write(sData)
            sunucuSocket.sendto("ACK".encode(), istemciAdres)
            sunucuSocket.settimeout(2)

            sData, istemciAdres = sunucuSocket.recvfrom(buf)

            print("Downloading from Relay Server...")
            print (sData)
        print("Download Completed")
        break
except Exception:
    print("Error happened!")
print("Time passed: " + str(time.time() - start_time))

sunucuSocket.close()
