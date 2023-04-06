def mencode(string)->str:
    a=''
    for i in string:
        # print(ord(i))
        a+=str(len(str(ord(i))))+str(ord(i))
    return a

def mdecode(string)->str:
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
filename="publicKey.tk1"

# For Encoding 
# with open(filename,"w") as keyFile:
#     keyFile.write(mencode(input("Enter Message to Encrypt: ")))

# # For Decoding
print("Searching for",filename,"file")
with open(filename) as keyFile:
    print(mdecode(keyFile.readline().strip()))
