#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        02-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
from cryptomodule import CryptoModule
from set1_testdata import set1_06_expected_result

cm = CryptoModule()

output = ''
cipher = cm.read_file_as_bytes('set1_06_cipher.txt')
cipher = cm.convert_base64_to_bytes(cipher)

output = cm.break_repeating_key_xor(cipher)
key = (output[0])[0].decode()
text = (output[0])[2].decode().strip()

print("Key: ", key, end='\r\n')
print("Text: ", text, end='\r\n')

if key == set1_06_expected_result:
    print("\nSuccess!")
    exit(0)
else:
    exit(-1)
