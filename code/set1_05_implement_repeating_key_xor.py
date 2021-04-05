#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        02-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
from cryptomodule import CryptoModule
from set1_testdata import set1_05_input_data, set1_05_expected_result


cm = CryptoModule()

output = ''

output = cm.encrypt_repeating_key_xor_hex(set1_05_input_data, 'ICE')

print(output)

if output == set1_05_expected_result:
    print("Success!")
    exit(0)
else:
    exit(-1)
