#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        20-03-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
import string
from base64 import b64encode

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


class Converter(object):

    output_base64 = b''
    output_xor = b''
    output_plain = ''
    plain_text_rating = 0.0
    best_rated_plain_text = ''
    best_rated_plain_text_key = None
    highest_plain_text_rating = 0

    def __init__(self, s_hex=''):
        self.load_hex_string(s_hex)

    def from_hexbytes_to_base64(self):
        """
        Convert bytes in hex format to base64
        Available at obj.output_base64
        """
        self.output_base64 = b64encode(self.bytes_s_hex)

    def load_hex_string(self, s_hex):
        """
        Load hex encoded string

        :param s_hex: hex encoded string
        :type s_hex: string
        """
        self.bytes_s_hex = bytes.fromhex(s_hex)

    def atoz_singlechar_brute_force(self, input_bytes_string):
        for char in range(ord('A'), ord('z')+1):
            self.produce_xor(input_bytes_string, char)
            self.rate_plain_text()

            if self.plain_text_rating > 1.0:
                print('\nKey: %c' % chr(char))
                print('Plain Text: %s' % self.output_plain)
                print('Rating: %f' % self.plain_text_rating)

        print("\nBest Rated Plain Text:")
        print('\nKey: %c' % chr(self.best_rated_plain_text_key))
        print('Plain Text: %s' % self.best_rated_plain_text)
        print('Rating: %f' % self.highest_plain_text_rating)

    def rate_plain_text(self):
        normal_char_set = string.ascii_letters + ' '
        chars = []

        for char in self.output_plain:
            if char in normal_char_set:
                chars.append(char)

        if chars is not None:
            text_to_rate = ''.join(chars)
            self.__rate_text(text_to_rate)

        else:
            self.output_plain = 'text did not make sense'

    def __rate_text(self, s):
        rating = 0.0
        len_plain_text = len(self.output_plain)

        if len_plain_text == len(s):
            rating = 1.0

        if len(s) > 0:
            rating += 0.01

        for c in s:
            rating += MOST_FREQUENT_LETTERS.get(c.lower(), 0)

        if rating > self.highest_plain_text_rating:
            self.highest_plain_text_rating = rating
            self.best_rated_plain_text = self.output_plain
            self.best_rated_plain_text_key = self.used_key

        self.plain_text_rating = rating

    # region XOR

    def produce_xor(self, b_hex1, b_hex2):
        """
        Takes two hex formatted byte strings to produce their XOR value to obj.output.xor
        If they are not equal lengths, then the shortest one will be padded with
        the last char in the shortest string

        :param b_hex1: hex string
        :type b_hex1: bytes
        :param b_hex2: hex string
        :type b_hex2: bytes
        """
        self.s1 = b_hex1
        self.s2 = b_hex2

        if type(self.s1) is int:
            self.__onebyte_key_xor(self.s2, self.s1)

        elif type(self.s2) is int:
            self.__onebyte_key_xor(self.s1, self.s2)

        else:
            self.s1_len = len(self.s1)
            self.s2_len = len(self.s2)

            if self.__inputs_are_not_same_length():
                print("Inputs are not equal length")
                return 0
            else:
                self.__equal_length_bytes_xor()

    def __inputs_are_not_same_length(self):
        return self.s1_len != self.s2_len

    def __equal_length_bytes_xor(self):
        self.s1 = int(self.s1, 16)
        self.s2 = int(self.s2, 16)
        bytes_hex = hex(self.s1 ^ self.s2)[2:]
        self.output_xor = bytes_hex.encode()
        self.__decode_hex_to_plaintext(bytes.fromhex(bytes_hex))

    def __onebyte_key_xor(self, b_input, key):
        self.used_key = key
        output = b''
        for char in b_input:
            output += bytes([char ^ key])

        self.__decode_hex_to_plaintext(output)

    # endregion XOR

    def __decode_hex_to_plaintext(self, b_hex):
        self.output_plain = b_hex.decode("utf-8")
