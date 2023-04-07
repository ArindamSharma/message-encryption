from getpass import getpass
from sys import argv
def mencode(string,privateKey)->str:
    # encrypting 
    e=""
    # print("Private Key: ",privateKey)
    # print("Message",string)
    for i in range(len(string)):
        x=ord(string[i])
        y=ord(privateKey[i%len(privateKey)])
        e+=hex(x+y)[2:]
        # print(hex(x+y)[2:],x+y,y,x)

    # print("Hexa",e)

    # # storage conversion
    # a="".join([str(len(str(ord(i))))+str(ord(i)) for i in string])
    # print("message Converted",a)
    a="".join([str(len(str(ord(i))))+str(ord(i)) for i in e])
    # print("hexa Converted",a)
    return a

# For Encoding

# default filename
filename="publicKey"

try:
    x=argv[1].split(".")
    if(len(x)>1):
        if(x[-1]=="tk2"):
            filename=argv[1]
        else:
            print("Wrong File Format")
            exit(1)
    else:
        filename=argv[1]+".tk2"
except IndexError:
    filename+=".tk2"

print("Will generate/update "+filename+" file")
with open(filename,"w") as keyFile:
    x=mencode(input("Enter Message to Encrypt\n"),getpass("Encryption privateKey: "))
    keyFile.write(x)
