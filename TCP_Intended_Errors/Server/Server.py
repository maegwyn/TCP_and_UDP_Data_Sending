import socket
from random import randint
from os import listdir

soket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #SOCK_STREAM is TCP, SOCK_DGRAM is UDP
soketB= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

path = "C:\\Users\\Burak\\PycharmProjects\\452ProjeSoru3\\Server"

HOST = "localhost"
PORT1 = 8000
PORT2 = 8500
buf = 1024
bFileFound = 0
clientA = False
temp = ""

counter = 0

soket.bind((HOST,PORT1))
server = (HOST, PORT2)

print (str(HOST)+" " + str(PORT1) +" server başlatıldı.")
print (str(HOST)+" " + str(PORT2) +" server başlatıldı.")

p = input("Enter package drop rate(0<p<1)") #package drop rate
q = input("Enter bit error rate(0<q<1)") #bit loss rate

while True:
    sData = "Temp"

    sData = soket.recv(buf)
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
        packageCounter = 0
        while sRead:
            sRead = fUploadFile.read(buf)
            packageCounter += 1 #to calculate how many packeges the data has

        fUploadFile = open(path + "\\" +  fileCropped, "rb")
        sRead = fUploadFile.read(buf)

        while sRead:
            chance = randint(0, 2)
            if counter != (float(p) - float(q))*packageCounter: #packets will be dropped here. q is substracted from q becouse p is total error rate
                if chance == 1 :
                    sRead = fUploadFile.read(buf)
                    print("Oops packet has been dropped!")
                    counter += 1
                else:
                    print("Sending file to B...")
                    soketB.sendto(sRead, server)
                    sRead = fUploadFile.read(buf)
                    #sRead = int(sRead[0])<< 1 ####shift işlemi olmuyor
                    #sRead = bytes(sRead)
            else:
                # print("Sending file...")
                soketB.sendto(sRead, server)
                sRead = fUploadFile.read(buf)
        soketB.sendto(sRead, server)
        print("Packets dropped: " + str(counter))
        print("Sending Completed")
        break
    break


soket.close()
