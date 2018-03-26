alphabet = "abcdefghijklmnopqrstuvwxyz"

#GET ORIGINAL LETTER POSITION
def alpha_pos(char):
    lowchar = char.lower()
    return alphabet.find(lowchar)

#GET ENCRYPTED LETTER
def rotate_char(char, rot):
    new_pos = (alpha_pos(char)+rot)%len(alphabet)
    if char.islower():
        return alphabet[new_pos]
    else:
        return alphabet[new_pos].upper()

#CAESAR ENCRYPTION METHOD
def caesar_encrypt(text,rot):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_text += rotate_char(char,rot)
        else:
            encrypted_text += char
    return encrypted_text