#!/usr/bin/env python
'''
    Author:        Daniel K. Vinther Wolf
    Created:       01-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
from base64 import b64encode, b64decode


class Converter(object):

    def __init__(self):
        pass

    # ==========================================
    # Hex Bytes as Input, Methods
    # ==========================================

    def convert_hex_to_base64(self, data):
        """
        Convert hex formated bytes to base64 encoding
        """
        data = self.convert_hex_bytes_to_string(data)
        return b64encode(data)

    def convert_hex_to_string(self, data):
        """
        Convert hex formated bytes to string
        """
        output = self.__remove_hex_prefix_if_present(data)
        output = output.decode()
        return bytes.fromhex(output).decode()

    def convert_hex_bytes_to_string(self, data):
        """
        Convert hex formated bytes to string
        """
        output = self.__remove_hex_prefix_if_present(data)
        output = output.decode()
        return bytes.fromhex(output)

    def convert_hex_to_string_bytes(self, data):
        """
        Convert hex formated bytes to string
        """
        output = self.__remove_hex_prefix_if_present(data)
        output = output.decode()
        return bytes.fromhex(output)

    # ==========================================
    # String as Input, Methods
    # ==========================================

    def convert_string_to_hex(self, string):
        """
        Convert string to hex formated bytes
        """
        output = ''

        for char in string:
            output += hex(ord(char))[2:]

        return output.encode()

    # ==========================================
    # Base64 as Input, Methods
    # ==========================================

    def convert_base64_to_string_bytes(self, b64):
        return b64decode(b64)

    # ==========================================
    # Aggregate Methods
    # ==========================================

    def __remove_hex_prefix_if_present(self, data):
        """
        Remove "0x" prefix if present
        """
        if b'0x' in data[:2]:
            return data[2:]
        else:
            return data
