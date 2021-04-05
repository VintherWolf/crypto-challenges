#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        02-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
from cryptomodule import CryptoModule
from set1_testdata import set1_07_expected_result

cm = CryptoModule()

output = ''
cipher = cm.read_file_as_bytes('set1_07_base64.txt')
cipher = cm.convert_base64_to_bytes(cipher)

key = b'YELLOW SUBMARINE'
output = cm.decrypt_aes_128b_ecb(cipher, key)
output = cm.convert_bytes_to_pretty_string_output(output)
print(output)

if set1_07_expected_result in output:
    print("\nSuccess!")
    exit(0)
else:
    print("\nFailed!")
    exit(-1)
