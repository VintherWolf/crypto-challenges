#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        20-03-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''


class Decrypter(object):

    hamming_distance = None

    def __init__(self):
        pass

    def compute_hamming_distance(self, s1, s2):

        if len(s1) != len(s2):
            print("Strings are must be equal lengths")
            return 0

        hamming_count = 0
        hamming_int = 0

        for s1_bn, s2_bn in zip(s1, s2):
            xor_value = bin(ord(s1_bn) ^ ord(s2_bn))

            for bit in xor_value:
                if bit is '1':
                    hamming_count += 1

        self.hamming_distance = hamming_count

    def __string_to_hex(self, string):
        s_hex = string.encode()
        return s_hex.hex().encode()
