import rsa
import symmetric_cipher

def main():
    print('Keys are generated using a prime integer pair. Enter a range to generate primes.')
    min = int(input('Min: '))
    max = int(input('Max: '))
    p,q = rsa.random_prime(min,max), rsa.random_prime(min,max)
    print('p and q values: ' + str(p) + ', ' + str(q))
    print('Key pairs generating...')
    public_key, private_key = rsa.generate_key(p,q)
    print('Public key: ' + str(public_key))
    print('Private key: ' + str(private_key))
    print('The public key can only encrypt values, whereas the private key can only decrypt values.')
    print('To send an encrypted message, an integer key can be used which would then be encrypted using the public key and sent with the message.')
    print('Note: the integer key must have a value less than n, the product of p and q.')
    key = symmetric_cipher.generate_random_key(public_key[0])
    print('For example: let the key be: ' + str(key))
    message = input('Enter a message to encrypt: ')
    encrypted_message = symmetric_cipher.encrypt_string(message,key)
    print('This message would be encrypted as "' + encrypted_message + '" using our key.')
    print('Next, this integer key can be used with the RSA encryption scheme using th public key.')
    encrypted_key = rsa.encrypt(key,public_key)
    print('The key ' + str(key) + ' encrypted using the public key is ' + str(encrypted_key) + '.')
    print ('This encrypted key and the encrypted message can be sent to the owner of the private key safely')
    print('')
    print('The owner of the private key can use it to decrypt the encypted key, and then use it on the cipher text:')
    unencrypted_key = rsa.decrypt(encrypted_key,private_key)
    print('Unencrypted key: ' + str(unencrypted_key) + '.')
    Unencrypted_message = symmetric_cipher.decrypt_string(encrypted_message,unencrypted_key)
    print('Unencrypted message: ' + Unencrypted_message + '.')

if __name__ == "__main__":
    main()
