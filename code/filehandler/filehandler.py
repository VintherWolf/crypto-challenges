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

    def read_file(self, filename):
        cipher_textfile = self.__set_path_to_code_dir(filename)
        try:
            with open(cipher_textfile, 'r') as cipher_text:
                return cipher_text.read().splitlines()

        except FileNotFoundError as ex:
            print("[FileHandler] Error: %s Not Found" % cipher_textfile)
            print(ex)
            raise

    def read_file_as_bytes(self, filename):
        cipher_textfile = self.__set_path_to_code_dir(filename)
        try:
            with open(cipher_textfile, 'r') as cipher_text:
                cipher = cipher_text.read()
                return cipher.encode()

        except FileNotFoundError as ex:
            print("[FileHandler] Error: %s Not Found" % cipher_textfile)
            print(ex)
            raise
    
    def read_file_as_hexbytes(self, filename):
        cipher_textfile = self.__set_path_to_code_dir(filename)
        cipher_texts = []
        try:
            with open(cipher_textfile, 'r') as cipher_text:
                for line in cipher_text:
                    cipher_texts.append(bytes.fromhex(line.strip()))
                return cipher_texts

        except FileNotFoundError as ex:
            print("[FileHandler] Error: %s Not Found" % cipher_textfile)
            print(ex)
            raise

    # ==========================================
    # Aggregate Methods
    # ==========================================

    def __set_path_to_code_dir(self, filename):
        abs_path = Path(__file__).parent.absolute()
        code_dir = str(abs_path.parent)+'\\'
        return code_dir + filename
