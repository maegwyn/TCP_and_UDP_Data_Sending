import socket
import os
from os import listdir
import hashlib
import time

start_time = time.time()


def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()
path = "C:\\Users\\Burak\\PycharmProjects\\452Proje\\Host1"
soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM is TCP, SOCK_DGRAM is UDP

HOST = "localhost"
PORT = 8000
buf = 1024
sFileName = ""
bFileFound = 0

soket.connect((HOST,PORT))

while True:
    sData = "Temp"
    sFileName = input("Enter file name to send: ")
    fileCropped = sFileName
    for file in listdir(path):
        if str(file) == fileCropped:
            bFileFound = 1
            break
    if bFileFound == 0:
        print(fileCropped + " Not Found On Server")
        statinfo = os.stat(fileCropped)

    else:
        print(fileCropped + " File Found")
        if os.path.getsize(path + "\\" + fileCropped) > 10485760:
            print("File size is too big!")
            continue;
        elif os.path.getsize(path + "\\" + fileCropped) < 1048576:
            print("File size is too small!")
            continue;
        else:
            fUploadFile = open(path + "\\" + fileCropped, "rb")
            sRead = fUploadFile.read(buf)
            while sRead:
                print("Sending to Server...")
                soket.send(sRead)
                sRead = fUploadFile.read(buf)

            sRead = fUploadFile.read(10485761)
            soket.send(str(computeMD5hash(str(sRead))).encode())
            print(str(computeMD5hash(str(sRead))).encode())
            break
    print("Sending Completed!")

soket.close()
print("Time passed: " + str(time.time() - start_time))
