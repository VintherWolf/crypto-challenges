#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        02-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
from cryptomodule import CryptoModule
from set1_testdata import set1_04_expected_result


cm = CryptoModule()

set1_04_input_data = cm.load_cipher_text_from_file('set1_04_cipher.txt')
output = []

output = cm.detect_encryption_by_singlechar_brute_force(set1_04_input_data)

print(output)

if output[0][2] == set1_04_expected_result:
    print("Success!")
    exit(0)
else:
    exit(-1)
