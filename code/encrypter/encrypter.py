#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:       31-03-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''


class Encrypter(object):

    def __init__(self):
        pass

    def encrypt_xor_repeating_key(self, text, key):

        keylen = len(key)
        output = b''

        if keylen < 1:
            print(
                "[Encrypter] Repeating Key XOr Failed: Key must be at least one char long!")
            return -1

        i = 0
        for _, char in enumerate(text):
            output += bytes([ord(char) ^ ord(key[i])])

            i += 1
            if i % keylen == 0:
                i = 0

        return output.hex().strip()
