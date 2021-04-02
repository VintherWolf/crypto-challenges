#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:       31-03-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''

from converter.converter import Converter
from decrypter.decrypter import Decrypter
from encrypter.encrypter import Encrypter
from filehandler.filehandler import FileHandler


class CryptoModule(Converter, Decrypter, Encrypter, FileHandler):

    def __init__(self):
        super()

    def singlechar_brute_force(self, data):
        """
        Execute brute force decryption on data (hex-formated cipher in bytes)
        with a single ASCII char at a time
        from 0 to 255 (see https://www.ascii-code.com/)
        data must be bytes.fromhex formatted (b'.\xf0\xf1\xf2')
        """
        xor_produced_text = b''
        rating = 0
        best_rating = -1
        output_array = []

        for ascii_decimal in range(0, 256):
            xor_produced_text = self.singlebyte_xor(data, ascii_decimal)
            plain_text = self.decode_if_needed(xor_produced_text)

            rating = self.rate_text(plain_text)

            if rating > best_rating:
                best_rating = rating
                # Output Array: [ 0:dec | 1:char | 2:rating | 3:plainText ]
                output_array.append([ascii_decimal, chr(
                    ascii_decimal), rating, plain_text])

        # Keep only top 5 Best Rated Texts, sorted decending rating
        output_array = sorted(
            output_array, key=lambda best: best[2], reverse=True)[:5]

        return output_array

    def detect_encryption_by_singlechar_brute_force(self, cipher):
        output_array = []
        best_rating_text = []

        for lines in cipher:
            if len(lines) > 2:
                line = lines.strip()
                line = bytes.fromhex(line)
                # Brute Force each line
                output_array = self.singlechar_brute_force(line)
                # Keep the key, rating and the decrypted text
                best_rating_text.append(
                    [output_array[0][0], output_array[0][2], output_array[0][3].strip()])

        # Keep only the top 3 best Rated Texts, sorted decending rating
        best_rating_text = sorted(
            best_rating_text, key=lambda best: best[1], reverse=True)[:3]
        return best_rating_text
