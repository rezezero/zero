from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad 
key = b'0123456789abcdef' 
plaintext = input("Enter Plain Text: ").encode() 
cipher = AES.new(key, AES.MODE_ECB)
# ENCRYPTION  
encrypted = cipher.encrypt(pad(plaintext, 16)) 
print("Encrypted:", encrypted.hex()) 
# DECRYPTION 
decrypted = unpad(cipher.decrypt(encrypted), 16) 
print("Decrypted:", decrypted.decode())