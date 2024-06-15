# Simple solution
key = 'QTGABCDEFHIJKOMNLPRSUVZYXW'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decrypt(mess, key):
    """
    This function decrypt the encrypted message with a key
    :param mess: encrypted message
    :param key: cipher key
    :return: decrypted message
    :return:
    """
    mess = mess.upper()
    new_str = ''
    for char in mess:
        if char.isalpha():  # or can check if char.upper() in key:
            index = key.find(char)
            e_char = alphabet[index]
            new_str = new_str + e_char
        else:
            new_str = new_str + char
    return new_str


print(decrypt('EBJJM ZMPJA $*^%$*', key))


# Another solution using the tricky ord() function (which is not good for special characters)
def substition_decipher(s, cipher):
    """
    This function decrypts the substitution cipher.
    :param s: a string, the message you want to decrypt
    :param cipher: the mapping of the 26 letters in the alphabet, e.g. “QTGABCDEFHIWKOJNMPUSRVXYZL"
    :return: the decrypted version of the message
    """
    s = s.upper()
    cipher = cipher.upper()
    print("original: ", s)
    encrypted_message = ''

    for i in range(len(s)):
        # find the index in the cipher
        cipher_index = cipher.find(s[i])  # index of the letter to use from the cipher
        decipher_index = cipher_index + 65  # int code for the letter A
        encrypted_message = encrypted_message + chr(decipher_index)  # chr() is the opposite function of ord()

    return encrypted_message


# main program
print('decrypted message', substition_decipher('EBWWJ', 'QTGABCDEFHIWKOJNMPUSRVXYZL'))
