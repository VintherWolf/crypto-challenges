#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        20-03-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
from base64 import b64encode


class Converter(object):

    output_base64 = b''
    output_xor = b''

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

    # region XOR
    def produce_xor(self, b_hex1, b_hex2):
        """
        Takes two hex formatted byte strings to produce their XOR value to obj.output.xor
        If they are not equal lengths, then the shortest one will be padded with 0'es

        :param b_hex1: hex string
        :type b_hex1: bytes
        :param b_hex2: hex string
        :type b_hex2: bytes
        """
        self.s1 = b_hex1
        self.s2 = b_hex2
        self.__make_inputs_equal_lenghts()
        self.__byte_xor()

    def __make_inputs_equal_lenghts(self):
        self.s1_len = len(self.s1)
        self.s2_len = len(self.s2)

        while self.__inputs_are_not_same_length():
            self.__add_padding()
            self.__recalculate_lenghts()

    def __inputs_are_not_same_length(self):
        return self.s1_len != self.s2_len

    def __add_padding(self):
        padding = b'0'
        if self.s1_len > self.s2_len:
            self.s2 += padding
        else:
            self.s1 += padding

    def __recalculate_lenghts(self):
        self.s1_len = len(self.s1)
        self.s2_len = len(self.s2)

    def __byte_xor(self):
        self.s1 = int(self.s1, 16)
        self.s2 = int(self.s2, 16)
        self.output_xor = hex(self.s1 ^ self.s2)[2:].encode()
    # endregion XOR
