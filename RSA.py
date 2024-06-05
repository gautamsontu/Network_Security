import random
from sympy import randprime
import time


class RSA:
    def __init__(self, keysize):
        self.keysize = keysize
        self.public_key = None
        self.private_key = None
        self.generate_keys()

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def modinv(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def generate_keys(self):
        # Generating two random prime numbers p and q
        p = randprime(2 ** (self.keysize // 2 - 1), 2 ** (self.keysize // 2))
        q = randprime(2 ** (self.keysize // 2 - 1), 2 ** (self.keysize // 2))
        n = p * q
        phi = (p - 1) * (q - 1)

        # Choosing e such that 1 < e < phi and gcd(e, phi) = 1
        e = random.randrange(2, phi)
        while self.gcd(e, phi) != 1:
            e = random.randrange(2, phi)

        # Computing d, the modular multiplicative inverse of e (mod phi)
        d = self.modinv(e, phi)

        # Public key (e, n) and private key (d, n)
        self.public_key = (e, n)
        self.private_key = (d, n)

    def encrypt(self, plaintext):
        e, n = self.public_key
        ciphertext = [pow(ord(char), e, n) for char in plaintext]
        return ciphertext

    def decrypt(self, ciphertext):
        d, n = self.private_key
        plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
        return plaintext


def main():
    keysize = int(input("Enter the key size: "))

    start_time = time.time()
    rsa = RSA(keysize)
    key_generation_time = time.time() - start_time

    print(f"Public Key: {rsa.public_key}")
    print(f"Private Key: {rsa.private_key}")
    print(f"Key generation time: {key_generation_time:.4f} secs")

    while True:
        choice = input("Choose an option: (1) Encrypt (2) Decrypt (3) Exit: ")

        if choice == '1':
            plaintext = input("Enter plaintext to encrypt: ")
            start_time = time.time()
            ciphertext = rsa.encrypt(plaintext)
            encryption_time = time.time() - start_time
            print(f"Ciphertext: {ciphertext}")
            print(f"Encryption time: {encryption_time:.4f} secs")

        elif choice == '2':
            ciphertext = input("Enter ciphertext to decrypt: ")
            try:
                ciphertext = list(map(int, ciphertext.strip('[]').split(',')))
                start_time = time.time()
                decrypted_text = rsa.decrypt(ciphertext)
                decryption_time = time.time() - start_time
                print(f"Decrypted Text: {decrypted_text}")
                print(f"Decryption time: {decryption_time:.4f} secs")
            except ValueError as e:
                print(f"Error: {e}.Entered wrong ciphertext.")

        elif choice == '3':
            break
        else:
            print("Invalid choice! Please choose again from the given options.")


if __name__ == "__main__":
    main()
