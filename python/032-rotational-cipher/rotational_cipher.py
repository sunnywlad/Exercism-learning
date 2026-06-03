def rotate(text, key):
    r_key = key % 26
    cipher_a = []
    for letter in text:
        if 97 <= ord(letter) <= 122:
            cipher_a.append(chr(((ord(letter) - 97 + r_key) % 26) + 97))
        elif 65 <= ord(letter) <= 90:
            cipher_a.append(chr(((ord(letter) - 65 + r_key) % 26) + 65))
        else:
            cipher_a.append(letter)
    return ''.join(cipher_a)
