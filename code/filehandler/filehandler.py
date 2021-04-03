#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:       31-03-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''

from pathlib import Path


class FileHandler(object):

    def __init__(self):
        pass

    def load_cipher_text_from_file(self, filename):
        cipher_textfile = self.__set_absolute_path(filename)
        try:
            with open(cipher_textfile, 'r') as cipher_text:
                return cipher_text.read().splitlines()

        except FileNotFoundError as ex:
            print("[FileHandler] Error: %s Not Found" % cipher_textfile)
            print(ex)
            raise

    def load_cipher_text_as_bytes_from_file(self, filename):
        cipher_textfile = self.__set_absolute_path(filename)
        try:
            with open(cipher_textfile, 'r') as cipher_text:
                cipher = cipher_text.read()
                return cipher.encode()

        except FileNotFoundError as ex:
            print("[FileHandler] Error: %s Not Found" % cipher_textfile)
            print(ex)
            raise

    # ==========================================
    # Aggregate Methods
    # ==========================================

    def __set_absolute_path(self, filename):
        abs_path = Path(__file__).parent.absolute()
        code_dir = str(abs_path.parent)+'\\'
        return code_dir + filename
