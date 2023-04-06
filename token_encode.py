from getpass import getpass
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
print("Will generate/update publicKey.tk2 file")
with open("publicKey.tk2","w") as keyFile:
    x=mencode(input("Enter Message to Encrypt\n"),getpass("Encryption privateKey: "))
    keyFile.write(x)
