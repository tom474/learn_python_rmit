# Simple solution
cipher_key = 'QTGABCDEFHIJKOMNLPRSUVZYXW'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(mess, key):
    """
    This function encrypt the message with a key
    :param mess: original message
    :param key: cipher key
    :return: encrypted message
    """
    mess = mess.upper()
    new_str = ''
    for char in mess:
        if char.isalpha():  # or can check if char.upper() in alphabet:
            index = alphabet.find(char)
            e_char = key[index]
            new_str = new_str + e_char
        else:
            new_str = new_str + char
    return new_str


print(encrypt('Hello World $*^%$*', cipher_key))


# Another solution using the tricky ord() function (which is not good for special characters)
def substitution_cipher(s, cipher):
    """
    This function encrypts the substitution cipher.
    :param s: a string, the message you want to encrypt
    :param cipher: the mapping of the 26 letters in the alphabet, e.g. “QTGABCDEFHIWKOJNMPUSRVXYZL"
    :return: the encrypted version of the message
    """
    s = s.upper()
    cipher = cipher.upper()
    print("original: ", s)

    encrypted_message = ''
    for i in range(len(s)):
        cipher_index = ord(s[i]) - 65  # index of the letter to use from the cipher
        encrypted_message = encrypted_message + cipher[cipher_index]

    return encrypted_message


# main program
print(ord('A'))  # 65
print('encrypted message:', substitution_cipher('hello', 'QTGABCDEFHIWKOJNMPUSRVXYZL'))
