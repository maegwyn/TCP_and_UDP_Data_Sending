import socket
import os
from os import listdir

soket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #SOCK_STREAM is TCP, SOCK_DGRAM is UDP

path = "C:\\Users\\Burak\\PycharmProjects\\452ProjeSoru3\\Host1"

HOST = "localhost"
PORT = 8000
buf = 1024
sFileName = ""
bFileFound = 0

server = (HOST, PORT)

while True:
    sData = "Temp"
    sFileName = input("Enter Filename to send : ")
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
        print("File size :" + str(os.path.getsize(path + "\\" + fileCropped)))
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
                print("Sending file to Server...")
                soket.sendto(sRead,server)
                sRead = fUploadFile.read(buf)
            soket.sendto(sRead, server)
            print("Sending Completed.")
            break
soket.close()