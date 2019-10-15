import sys
import random

def main(argv):
    try:
        option, message, key = argv[0], argv[1], int(argv[2])
    except:
        print('Usage: symmetric_cipher.py <option> <message> <key>')
        sys.exit(2)
    if option == 'encrypt':
        print(encrypt_string(message,key))
    elif option == 'decrypt':
        print(decrypt_string(message,key))
    else:
        print('Usage: symmetric_cipher.py <encrypt or decrypt> <message> <key>')

def encrypt_char(char,key):
    # Encrypts char input using an integer key and caesar cipher
    val = ord(char)
    val += key
    while val > 126:
        val -= 95
    return chr(val)

def decrypt_char(char,key):
    # Decrypts char input using an integer key and caesar cipher
    return encrypt_char(char,95-key)

def lengthen_key(key,length):
    # Returns int value of key that is longer than parameter length by concatenating
    new_key = str(key)
    while len(new_key) < length:
        new_key += str(key)
    return int(new_key)

def encrypt_string(message,key):
    # Encrypts string message using encrypt_char method and parameter key
    if len(str(key)) < len(message)*2:
        key = lengthen_key(key,len(message)*2)
    key = str(key)
    encrypted_message = ''
    for i in range(len(message)):
        encrypted_message += encrypt_char(message[i],int(key[(2*i):(2*i)+2]))
    return encrypted_message

def decrypt_string(message,key):
    # Decryts string message using decrypt_char method and parameter key
    if len(str(key)) < len(message)*2:
        key = lengthen_key(key,len(message)*2)
    key = str(key)
    encrypted_message = ''
    for i in range(len(message)):
        encrypted_message += decrypt_char(message[i],int(key[(2*i):(2*i)+2]))
    return encrypted_message

def generate_random_key(max):
    # Returns an integer value of a key less than the value of parameter max
    return random.randrange(max)

if __name__ == "__main__":
    main(sys.argv[1:])
