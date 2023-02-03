def caesar_cipher(ciphertext, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            idx = shifted_alphabet.find(char.lower())
            if char.isupper():
                plaintext += alphabet[idx].upper()
            else:
                plaintext += alphabet[idx]
        else:
            plaintext += char
    return plaintext

ciphertext = input("解読したい文字を打て ")
shift = 7
print(caesar_cipher(ciphertext, shift))
