import socket
from os import listdir
import time

soket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #SOCK_STREAM is TCP, SOCK_DGRAM is UDP
soketB= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

path = "C:\\Users\\Burak\\PycharmProjects\\452ProjeUDP\\Server"

HOST = "localhost"
PORT1 = 8000
PORT2 = 8500
buf = 1024
bFileFound = 0
clientA = False
temp = ""
start_time = 0

soket.bind((HOST,PORT1))

server = (HOST, PORT2)


print (str(HOST)+" " + str(PORT1) +" server başlatıldı.")
print (str(HOST)+" " + str(PORT2) +" server başlatıldı.")


while True:
    sData = "Temp"

    sData = soket.recv(buf)
    start_time = time.time()

    fDownloadFile = open("burak", "wb")
    try:
        while sData:
            fDownloadFile.write(sData)
            sData = soket.recv(buf)
            soket.settimeout(2)

            print("Downloading from A...")
        print("Download Completed")
    except Exception:
        print("Error happened!")
    fileCropped = "burak"
    for file in listdir(path):
        if str(file) == fileCropped:
            bFileFound = 1
            break
    if bFileFound == 0:
        print(fileCropped + " Not Found On Server")
    else:
        print(fileCropped + " File Found")

        fUploadFile = open(path + "\\" + fileCropped, "rb")
        sRead = fUploadFile.read(buf)
        while sRead:
            print("Sending file to B...")
            soketB.sendto(sRead, server)
            sRead = fUploadFile.read(buf)
        soketB.sendto(sRead, server)
    print("Sending Completed")
    break

print("Time passed: " + str(time.time() - start_time))

soket.close()