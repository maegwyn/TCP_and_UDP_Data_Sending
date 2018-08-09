from socket import *
from os import listdir
import os
import time

path = "C:\\Users\\Burak\\PycharmProjects\\Bil452UDP2\\Host1\\"
sunucuAd = 'localhost'
sunucuPort = 12345
buf = 1024
istemciSocket = socket(AF_INET, SOCK_DGRAM) #datagram
while True:
    fileCropped = input("Gonderilecek dosyayi giriniz: ")
    start_time = time.time()

    for file in listdir(path):
        if str(file) == fileCropped:
            bFileFound = 1
            break
    if bFileFound == 0:
        print(fileCropped + " Not Found On Server")
        statinfo = os.stat(fileCropped)

    else:
        print(fileCropped + " File Found")
        print(os.path.getsize(path + fileCropped))
        if os.path.getsize(path + fileCropped) > 10485760:
            print("File size is too big!")
            continue;
        elif os.path.getsize(path + fileCropped) < 1048576:
            print("File size is too small!")
            continue;
        else:
            fUploadFile = open(path + fileCropped, "rb")
            sRead = fUploadFile.read(buf)
            while sRead:
                print("Sending file to Relay Server...")
                istemciSocket.sendto(sRead, (sunucuAd, sunucuPort))

                yeniMesaj, sunucuAdres = istemciSocket.recvfrom(buf)
                print(str(yeniMesaj)[2:5])
                if(str(yeniMesaj)[2:5] != "ACK"):
                    print("Hata")
                    istemciSocket.sendto(sRead, (sunucuAd, sunucuPort)) #ACK alinamaz ise aynı paket tekrar gönderilir.
                    continue
                sRead = fUploadFile.read(buf)
                print(sRead)
            istemciSocket.sendto(sRead, (sunucuAd, sunucuPort))
            break
print("Time passed: " + str(time.time() - start_time))

istemciSocket.close()