from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP 
# Key generation 
key = RSA.generate(2048) 
public_key = key.publickey() 
message = input("Enter Message: ").encode() 
# ENCRYPTION 
cipher = PKCS1_OAEP.new(public_key) 
encrypted = cipher.encrypt(message) 
print("Encrypted:", encrypted.hex()) 
# DECRYPTION 
cipher = PKCS1_OAEP.new(key) 
decrypted = cipher.decrypt(encrypted) 
print("Decrypted:", decrypted.decode())