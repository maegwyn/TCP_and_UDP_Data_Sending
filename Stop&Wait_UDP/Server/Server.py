from socket import *
from os import listdir
import os
import time
start_time = time.time()

sunucuAd = 'localhost'
sunucuPort = 12345
buf = 1024
sunucuPort2 = 12346

path = "C:\\Users\\Burak\\PycharmProjects\\Bil452UDP2\\Server"

sunucuSocket = socket(AF_INET, SOCK_DGRAM)
istemciSocket = socket(AF_INET, SOCK_DGRAM)

sunucuSocket.bind((sunucuAd,sunucuPort))
print ('Sunucu veri almaya hazırdır.')
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

            print("Downloading From A...")
            print (sData)
        print("Download Completed")
        break

except Exception:
    print("Error happened!")

while True:
    fileCropped = "burak"
    for file in listdir(path):
        if str(file) == fileCropped:
            bFileFound = 1
            break
    if bFileFound == 0:
        print(fileCropped + " Not Found On Server")
    else:
        print(fileCropped + " File Found")

        fUploadFile = open(path+"\\" + fileCropped, "rb")
        sRead = fUploadFile.read(buf)
        while sRead:
            print("Sending file...")
            istemciSocket.sendto(sRead, (sunucuAd, sunucuPort2))

            yeniMesaj, sunucuAdres = istemciSocket.recvfrom(buf)
            print(str(yeniMesaj)[2:5])
            if (str(yeniMesaj)[2:5] != "ACK"):
                print("Hata")
                istemciSocket.sendto(sRead, (sunucuAd, sunucuPort2)) #ACK alinamaz ise aynı paket tekrar gönderilir.
                continue
            sRead = fUploadFile.read(buf)
            print(sRead)
        istemciSocket.sendto(sRead, (sunucuAd, sunucuPort2))
        break
    print("Sending Completed")
print("Time passed: " + str(time.time() - start_time))

sunucuSocket.close()
