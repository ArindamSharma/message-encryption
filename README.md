# message-encryption
Encrypt Message

## token_encrypt_v1.py script
this token standard conversion of a message to encrypted and decrypted message 
it generate a publickey which 
```
python token_encrypt.py <mode="encode"|"decode"> <filename>
```

## token_encode_v2.py scripts
this scripts are made in contunation of the previous script just added another encryption concept of public key and private key.
```
python token_encode.py <mode="encode"|"decode"> <filename>
```

## .tk1 files
version 1 type of file consist of encrypted key
## .tk2 files
version 2 type of file consist of publickey which can only be decrypted with a privatekey