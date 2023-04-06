from getpass import getpass
from sys import argv
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


# For Decoding publicKey.tk2

# default filename
filename="publicKey.tk2"
try:
    if(argv[1].split(".")[-1]=="tk2"):
        filename=argv[1]
    else:
        print("Wrong File Format")
        exit(1)
except:
    pass

try:
    with open(filename ,"r") as keyFile:
        print(mdecode(keyFile.readline().strip(),getpass("Decryption privateKey: ")))
except FileNotFoundError as e:
    print(e)
