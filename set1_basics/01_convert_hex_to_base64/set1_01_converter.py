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

    encoding_format = 'utf-8'
    output_base64 = ''

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
