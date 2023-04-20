def caesar_cipher(plaintext, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            idx = alphabet.find(char.lower())
            if char.isupper():
                ciphertext += shifted_alphabet[idx].upper()
            else:
                ciphertext += shifted_alphabet[idx]
        else:
            ciphertext += char
    return ciphertext

plaintext = input("何を隠したい？ ")
shift = input("なん文字ずらしたい？")
print(caesar_cipher(plaintext, shift))
