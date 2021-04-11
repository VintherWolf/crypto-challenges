#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        08-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
from cryptomodule import CryptoModule
from set1_testdata import set1_07_expected_result

cm = CryptoModule()
output = ''
key = b'YELLOW SUBMARINE'
test = []
cipher = cm.read_file_as_hexbytes('set1_08_hexCiphers.txt')

for i in range(len(cipher)):
    output = cm.attempt_to_break_aes_in_ecb_mode(cipher[i], key)

    if output is not None:
        print(output)

        if b'\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83' in output[1]:
            print("\nSuccess!")
            exit(0)

        else:
            print("\nFailed!")

