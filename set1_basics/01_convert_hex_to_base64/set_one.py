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

    def __init__(self, hex_string):
        # Convert hex string to byte format
        self.bytes_hex_string = bytes.fromhex(hex_string)

    def from_hexbytes_to_base64(self):
        self.output_base64 = b64encode(self.bytes_hex_string)
