#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:       31-03-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''

from itertools import combinations
from Crypto.Cipher.AES import block_size

from converter.converter import Converter
from decrypter.decrypter import Decrypter
from encrypter.encrypter import Encrypter
from filehandler.filehandler import FileHandler


class CryptoModule(Converter, Decrypter, Encrypter, FileHandler):

    def __init__(self):
        super()

    def singlechar_brute_force(self, data):
        """singlechar_brute_force

        Execute brute force decryption on data (hex-formated cipher in bytes)
        with a single ASCII char at a time
        from 0 to 255 (see https://www.ascii-code.com/)
        data must be bytes.fromhex formatted (b'.\xf0\xf1\xf2')

        :param data: bytes

        :type data: [ int | chr | float | str ]

        :return: [ 0:dec | 1:char | 2:rating | 3:plainText ]

        :rtype: list
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

    def break_repeating_key_xor(self, cipher):
        """break_repeating_key_xor [summary]

        :param cipher: cipher text

        :type cipher: Bytes

        :return: [key, rating, text]

        :rtype: Bytes
        """
        key_ranking = [[100, 100]]*5
        output_array = []

        cipherlen = len(cipher)

        # Try the keys on a relative long part of the cipher text
        patch_of_cipher = int(round(cipherlen / 10, 0))

        for key in range(2, patch_of_cipher):
            acum_distance = 0
            chunks = []

            chunks.append(cipher[0:key])
            chunks.append(cipher[key:2*key])
            chunks.append(cipher[2*key:3*key])
            chunks.append(cipher[3*key:4*key])

            # Possible combinations is saved in bins
            # ABCD = AB, AC, AD, BC, BD, CD (hence: there is 6 bins in total)
            bins = combinations(chunks, 2)
            num_of_bins = 6

            for (a, b) in bins:
                # Compute Hamming Distance
                acum_distance = self.compute_hamming_distance(a, b)

            avg_distance = acum_distance / num_of_bins

            # Normalize Hamming distance
            nom_distance = round(avg_distance / key, 2)

            key_ranking.append([key, nom_distance])

        # Key Sizes to try-out: key_ranking[0-2][dont care]
        key_ranking = sorted(key_ranking, key=lambda k: k[1])[:3]

        for row in key_ranking:
            key_size = (row)[0]
            tried_key = b''

            # Only try the Key (int) not the nom_distance (float) from the 2d-array
            if type(key_size) is int:
                for length in range(key_size):
                    block = b''

                    for nblock in range(length, cipherlen, key_size):
                        block += bytes([cipher[nblock]])

                    key_text = []
                    key_text = self.singlechar_brute_force(block)
                    tried_key += ((key_text)[0][1]).encode()

                plain_text = self.encrypt_repeating_key_xor_plain(
                    cipher, tried_key)

                rating = self.rate_text(plain_text)

                output_array.append(
                    [tried_key, rating, plain_text])

                output_array = sorted(
                    output_array, key=lambda k: k[1], reverse=True)[:3]
            else:
                continue

        return output_array

    # ==========================================
    # AES ECB Mode, Detect
    # ==========================================

    def dissect_data_in_block_sized_bites(self, data):
        # Need: from Crypto.Cipher.AES import block_size
        data_bites = []
        
        for i in range(0, len(data), block_size):
            data_bites.append(data[i:i + block_size])

        return data_bites
    
    def number_of_duplicates_in_datablocks(self, blocks_of_data):
        repeated = []

        unique_ciphers = set(blocks_of_data)
        num_of_ciphers = len(blocks_of_data)
        num_of_unique_ciphers = len(unique_ciphers)

        diff = num_of_ciphers - num_of_unique_ciphers

        if diff > 0:
            print('AES ECB Mode, Detected. Cipher is repeated ',diff, 'times')

            for i in range(num_of_ciphers):
                k = i + 1

                for j in range(k, num_of_ciphers):
                    if blocks_of_data[i] == blocks_of_data[j] and blocks_of_data[i] not in repeated: 
                        repeated.append(blocks_of_data[i])

            if repeated == []:
                repeated = None
        return repeated

    def attempt_to_break_aes_in_ecb_mode(self, data, key=b'YELLOW SUBMARINE'):

        next_result = b''
        last_result = b''

        plain_text = b''

        keylen = len(key)
        data_bites = []
        detected_ecb = ['AEC ECB Mode Ciphers Detected:']
            
        data_bites = self.dissect_data_in_block_sized_bites(data)

        detected_ecb.append(self.number_of_duplicates_in_datablocks(data_bites))

        if detected_ecb[1] == []:
            return None

        '''
        for block in data_bites:
            print("Block:", block)
            if type(block) is int:
                continue
            for line in block:
                print("Line:", line)
                for i in range(2):

                    next_result = b''
                    next_result = self.decrypt_aes_128b_ecb(line, key)

                    if last_result != b'':

                        if last_result == next_result:
                            rating = 0
                            rating = self.rate_text(next_result)
                            # Save This result as a possible ecb mode
                            possible_ecb = {
                                'cipher': line,
                                'plain_text': next_result,
                                'rating': rating
                            }

                            print("Possible ECB Match Detected: Cipher = ", possible_ecb['cipher'])
                            detected_ecb.append(possible_ecb)

                    if next_result != b'':

                        last_result = next_result
        detected_ecb = sorted(detected_ecb, key=lambda k: k['rating'], reverse=True)
        '''
        return detected_ecb
