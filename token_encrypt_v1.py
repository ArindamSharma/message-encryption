from sys import argv
def mencode(string:str)->str:
    a=''
    for i in string:
        # print(ord(i))
        a+=str(len(str(ord(i))))+str(ord(i))
    return a

def mdecode(string:str)->str:
    # storage conversion
    a=""
    i=0
    while(i<len(string)):
        clen=int(string[i])
        # print(i,i+clen+1)
        a+=chr(int(string[i+1:i+clen+1]))
        i=i+1+clen
    return a

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
        if(x[-1]=="tk1"):
            filename= argv[2]
        else:
            raise TypeError("Unsupported File Type : "+argv[2])
    else:
        filename=argv[2]+".tk1"

except IndexError:
    filename+=".tk1"

# For Encoding 
if(toggle): 
    print("Will Generate/Update",filename,"file")
    with open(filename,"w") as keyFile:
        keyFile.write(mencode(input("Enter Message to Encrypt: ")))

# For Decoding
else:
    print("Reading/Searching for",filename,"file")
    with open(filename) as keyFile:
        print("\n",mdecode(keyFile.readline().strip()))