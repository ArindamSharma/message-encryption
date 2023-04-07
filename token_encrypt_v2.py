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

def mdecode(string,privateKey)->str:
    # print("Private Key: ",privateKey)
    # storage conversion
    a=""
    i=0
    while(i<len(string)):
        try:
            clen=int(string[i])
        except:
            print("Invalid Encrypted Message")
            exit(1)

		# print(i,i+clen+1)
        a+=chr(int(string[i+1:i+clen+1]))
        i=i+1+clen
    # print("Converted back: ",a)

    # decrepting
    p=""
    for i in range(0,len(a),2):
        s=int(a[i:i+2],16)
        y=ord(privateKey[int(i/2)%len(privateKey)])
        # print(a[i:i+2],s,y,s-y,chr(s-y))
        p+=chr(s-y)
    return p

# public Key
filename="publicKey"

#  Toggle switch
# 0 -> for encoding/encrypting
# 1-> for decoding/decrypting
toggle=0

try:
    if(argv[1] in ["encrypt","encode"]):
        toggle=1
    elif(argv[1] in ["decrypt","decode"]):
        toggle=0
    else:
        print("Invalid Switch Condition")
        exit(1)

    # filename validation/correction
    x=argv[2].split(".")
    if(len(x)>1):
        if(x[-1]=="tk2"):
            filename= argv[2]
        else:
            raise TypeError("Unsupported File Type : "+argv[2])
    else:
        filename=argv[2]+".tk2"

except IndexError:
    filename+=".tk2"

# For Encoding 
if(toggle): 
    print("Will Generate/Update",filename,"file")
    with open(filename,"w") as keyFile:
        keyFile.write(mencode(input("Enter Message to Encrypt\n"),getpass("Encryption privateKey: ")))

# For Decoding
else:
    print("Reading/Searching for",filename,"file")
    with open(filename) as keyFile:
        print("\n",mdecode(keyFile.readline().strip(),getpass("Decryption privateKey: ")))