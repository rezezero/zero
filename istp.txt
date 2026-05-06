message = input("Enter message: ")
key = int(input("Enter key: "))

# ENCRYPTION
cipher=""
for col in range(key):
    for i in range(col,len(message),key):
        cipher+=message[i]

print("Encrypted Message:", cipher)

# DECRYPTION
plain=[""]*key
index =0

for col in range(key):
    for i in range(col,len(message),key):
        plain[col]+=cipher[index]
        index+=1

decrypted=""
for i in range(len(message)):
    decrypted+=plain[i%key][i//key]

print("Decrypted Message:", decrypted)
