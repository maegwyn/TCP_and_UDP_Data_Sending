import socket
import time
import hashlib

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()
path = "C:\\Users\\Burak\\PycharmProjects\\452Proje\\Host2\\"
start_time = time.time()

soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM is TCP, SOCK_DGRAM is UDP
HOST = "localhost"
PORT = 8500
buf = 1024
sFileName = ""

soket.connect((HOST,PORT))
print("Ready to recieve file")

while True:
    sData = "Temp"
    sHash = "Temp"
    recievedHash = "Temp"
    hashedValue = "Temp"
    sRead = "Temp"

    sData = soket.recv(buf)

    fDownloadFile = open("burak", "wb")
    while sData:
        fDownloadFile.write(sData)
        sData = soket.recv(buf)
        print(sData)
        print("Downloading from Server...")
        if(str(sData)[2].isdigit()):    #recieving hash of recieved file from client
            recievedHash = str(sData)[2:str(sData).__len__()-1];
    print("Download Completed")

    fReadFile = open(path + "burak", "rb")
    sRead = str(fReadFile.read(10485761))

    if (recievedHash != hashedValue):   #comparing two hashes

        print("Recieved file is good!")

    break
print("Time passed: " + str(time.time() - start_time))


soket.close()