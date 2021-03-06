#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:       31-03-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


class Encrypter(object):

    def __init__(self):
        pass

    def encrypt_repeating_key_xor_hex(self, text, key):
        """
        XOR Encrypt text with key byte-by-byte and
        repeat until end of text

        Text input as hex bytes
        """
        keylen = len(key)
        output = b''
        text = self.encode_if_needed(text)
        key = self.encode_if_needed(key)

        if keylen < 1:
            print(
                "[Encrypter] Repeating Key XOr Failed: Key must be at least one char long!")
            return -1

        i = 0
        for _, char in enumerate(text):
            output += bytes([char ^ key[i]])

            i += 1
            if i % keylen == 0:
                i = 0

        return output.hex().strip()

    def encrypt_repeating_key_xor_plain(self, text, key):
        """
        XOR Encrypt text with key byte-by-byte and
        repeat until end of text

        Text input as plain text
        """
        keylen = len(key)
        output = b''
        text = self.encode_if_needed(text)
        key = self.encode_if_needed(key)

        if keylen < 1:
            print(
                "[Encrypter] Repeating Key XOr Failed: Key must be at least one char long!")
            return -1

        i = 0
        for _, char in enumerate(text):
            output += bytes([char ^ key[i]])

            i += 1
            if i % keylen == 0:
                i = 0

        return output

    # ==========================================
    # AES ECB Mode
    # ==========================================

    def encrypt_aes_128b_ecb_mode(self, data, key):
        cipher = AES.new(key, AES.MODE_ECB)
        # Add padding as described in at link:
        # https://www.pycryptodome.org/en/latest/src/cipher/classic.html#ecb-mode
        return cipher.encrypt(pad(data, AES.block_size, style='pkcs7'))

    # ==========================================
    # AES CBC Mode
    # ==========================================
    def xor_data(self, bin_data_1, bin_data_2):
        return bytes([b1 ^ b2 for b1, b2 in zip(bin_data_1, bin_data_2)])

    def encrypt_aes_128b_cbc_mode(self, data, key, iv):

        output = b''

        for i in range(0, len(data), AES.block_size):
            this_block = set_pkcs7_padding(
                data[i:i + AES.block_size], AES.block_size)
            block_cipher_input = self.xor_data(this_block, prev)
            encrypted_block = self.encrypt_aes_128b_ecb_mode(
                block_cipher_input, key)
            output += encrypted_block
            prev = encrypted_block

        return output

    # ==========================================
    # Aggregate Methods
    # ==========================================

    def encode_if_needed(self, input_data):
        if type(input_data) is str:
            return input_data.encode()
        else:
            return input_data

    def set_pkcs7_padding(self, text, block_size):
        output = ''
        padding = bytes.fromhex('04')

        padding_len = evaluate_padding_need(text, block_size)
        padding *= padding_len
        text = text + padding

        return text

    def evaluate_padding_need(self, text, block_size):

        padding_len = 0
        text_len = len(text)

        while (text_len % block_size != 0):
            text_len += 1
            padding_len += 1

        return padding_len
