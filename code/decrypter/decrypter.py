#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:       31-03-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from string import ascii_letters
from binascii import unhexlify, hexlify


class Decrypter(object):

    def __init__(self):
        pass

    def compute_hamming_distance(self, bin_s1, bin_s2):
        """
        compute the hamming distance between two binary sequences as inputs
        eg. 1010 ^ 1100 = 2 , 0010 ^ 0000 = 1 and 0010 ^ 0010 = 0
        Check for example by https://www.hacksparrow.com/tools/calculators/hamming-distance.html
        """
        if len(bin_s1) != len(bin_s2):
            print("Input bin_s1 and bin_s2 must be equal length")
            return -1

        hamming_distance = 0

        for bit_s1, bit_s2 in zip(bin_s1, bin_s2):
            xor_product = bit_s1 ^ bit_s2

            for bit in bin(xor_product):
                if bit is '1':
                    hamming_distance += 1

        return hamming_distance

    def rate_text(self, text):
        """
        Rates a plain text to see if it could be a human "readable" text
        """
        rating = 0.0
        space = ' '
        normal_chars = ascii_letters + space

        text = self.decode_if_needed(text)

        for char in text:
            if char in normal_chars:
                rating += MOST_FREQUENT_LETTERS.get(char.lower(), 0)
            if char in WIERD_LETTERS:
                rating += WIERD_LETTERS.get(char.lower(), 0)

        for word in COMMON_WORDS:
            if word in text.lower():
                rating += COMMON_WORDS.get(word)

        return round(rating, 2)

    # ==========================================
    # Simple XOR Decryption
    # ==========================================

    def singlebyte_xor(self, data, key):
        """
        Each byte in data is XOR'ed with the key
        data must be in bytes and
        key must be type(int)
        """
        output = b''

        key = self.validate_key(key)

        for char in data:
            output += bytes([char ^ key])

        return output

    def equal_length_inputs_xor(self, data_in1, data_in2):
        """
        Each data input mut be equal length
        data must be in bytes and hex formated
        """
        output = b''

        data_in1 = self.validate_data_input(data_in1)
        data_in2 = self.validate_data_input(data_in2)

        if len(data_in1) != len(data_in2):
            # TODO log error inputs must be equal length
            Exception("Input must be equal lengths")
            exit - 1
        else:
            data_in1 = int(data_in1, 16)
            data_in2 = int(data_in2, 16)
            output = hex(data_in1 ^ data_in2)[2:].encode()

        return output

    # ==========================================
    # AES ECB Mode
    # ==========================================

    def decrypt_aes_128b_ecb(self, cipher, key):
        """ 
        Returns a '16 Bytes key' decrypted ECB cipher
        Read more at https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html
        :return: ECB cipher object
        :rtype: object
        """
        decipher = AES.new(key, AES.MODE_ECB)
        plain_text = b''

        try:
            plain_text = unpad(decipher.decrypt(cipher), AES.block_size)
        except ValueError:
            print("[Decrypter] AES ECB Mode: Value/Text Error")
        except KeyError:
            print("[Decrypter] AES ECB Mode: Key Error")

        return plain_text

    # ==========================================
    # Aggregate Methods
    # ==========================================

    def decode_if_needed(self, input_data):
        if type(input_data) is bytes:
            input_data = self.remove_hex_prefix_if_present(input_data)
            return input_data.decode('utf-8', 'ignore')
        else:
            return input_data

    def validate_key(self, input_key):

        while type(input_key) is not int:

            if type(input_key) is bytes:
                input_key = input_key.decode()

            if type(input_key) is str:
                input_key = ord(input_key)

            else:
                pass
                # TODO log error input key must be int

        return input_key

    def validate_data_input(self, data):
        data_type = type(data)

        if data_type is bytes:
            data = self.remove_hex_prefix_if_present(data)
            data = data.decode()

        return data

    def remove_hex_prefix_if_present(self, data):
        """
        Remove "0x" prefix if present
        """
        if b'0x' in data[:2]:
            return data[2:]
        else:
            return data

    # ==========================================
    # Resources
    # ==========================================


# Values resembles those from
# source: https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
MOST_FREQUENT_LETTERS = {
    'e':    0.11,   'a':    0.085, 'r':  0.075,
    'i':    0.075,  'o':    0.072,  't':    0.069,
    'n':    0.066,  's':    0.057,  'l':    0.055,
    'c':    0.045,  'u':    0.036,  'd':    0.034,
    'p':    0.032,  'm':    0.031,  'h':    0.030,
    'g':    0.025,  'b':    0.021,  'f':    0.018,
    'y':    0.018,  'w':    0.013,  'k':    0.011,
    'v':    0.010,  'x':    0.002,  'z':    0.002,
    'j':    0.002,  'q':    0.002,  ' ':    0.05
}


WIERD_LETTERS = {
    '<': -0.3,   '>': -0.3, '&': -0.2,
    '\\': -0.3,  '/': -0.3,  '+': -0.3,
    '"': -0.3
}


# 0.2 value per letter in word (subjective measure)
# Max: 3.6
COMMON_WORDS = {
    'the':  0.6,    'and':  0.6,
    'that': 0.8,    'have': 0.8,   'this': 0.8
}
