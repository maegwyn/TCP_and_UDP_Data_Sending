import socket
from os import listdir
import time
import hashlib

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()
start_time = time.time()

path = "C:\\Users\\Burak\\PycharmProjects\\452Proje\\Server"
soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM is TCP, SOCK_DGRAM is UDP
soketB= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = "localhost"
PORT1 = 8000
PORT2 = 8500
buf = 1024
bFileFound = 0
clientA = False
temp = ""

soket.bind((HOST,PORT1))
soketB.bind((HOST,PORT2))

print (str(HOST)+" " + str(PORT1) +" server başlatıldı.")
print (str(HOST)+" " + str(PORT2) +" server başlatıldı.")

print ("Kullanıcı bekleniyor.")
soket.listen(5)
soketB.listen(5)

baglanti,adres = soket.accept()
baglanti2,adres2 = soketB.accept()
print ("Iki bağlantı kabul edildi. Birinci: " + str(adres) + " + Ikinci: " +str(adres2))

sDataLast = ""
fileCropped = "burak"
while True:
    sData = "Temp"
    sHash = "Temp"
    recievedHash = "Temp"
    hashedValue = "Temp"

    sData = baglanti.recv(buf)

    fDownloadFile = open("burak", "wb")
    while sData:
        fDownloadFile.write(sData)
        sData = baglanti.recv(buf)
        print("Downloading from A...")
        print
        if(str(sData)[2].isdigit()):    #recieving hash of recieved file from client
            recievedHash = str(sData)[2:str(sData).__len__()-1];
    print("Download Completed")

    fReadFile = open(path + "\\burak", "rb")
    sRead = str(fReadFile.read(10485761))

    hashedValue = str(computeMD5hash(str(sRead)))    #hashing recieved file
    if (recievedHash != hashedValue):   #comparing two hashes
        print("Recieved file is good!")


    for file in listdir(path):
        if str(file) == fileCropped:
            bFileFound = 1
            break
    if bFileFound == 0:
        print(fileCropped + " Not Found On Server")
    else:
        print(fileCropped + " File Found")

        fUploadFile = open(path +"\\" + fileCropped, "rb")
        sRead = fUploadFile.read(buf)
        while sRead:
            print("Sending to B...")
            baglanti2.send(sRead)
            sRead = fUploadFile.read(buf)
        print("Sending Completed!")
        sRead = fUploadFile.read(10485761)
        hashedValue = str(computeMD5hash(str(sRead))).encode()
        baglanti2.send(str(computeMD5hash(str(sRead))).encode())
        print("Recieved hash from Server: " + str(recievedHash))
        print("Calculated hash : " + str(hashedValue))
        break
    break
print("Time passed: " + str(time.time() - start_time))

soket.close()