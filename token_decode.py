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
filename="publicKey"
try:
    x=argv[1].split(".")
    if(len(x)>1):
        if(x[-1]=="tk2"):
            filename=argv[1]
        else:
            raise TypeError("Wrong File Format")
    else:
        filename=argv[1]+".tk2"
except IndexError:
    filename+=".tk2"

try:
    with open(filename ,"r") as keyFile:
        print(mdecode(keyFile.readline().strip(),getpass("Decryption privateKey: ")))
except FileNotFoundError as e:
    print(e)
