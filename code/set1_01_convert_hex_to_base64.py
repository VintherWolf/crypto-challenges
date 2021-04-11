#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        02-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
from cryptomodule import CryptoModule
from set1_testdata import set1_01_input_data, set1_01_expected_result


cm = CryptoModule()
base64_output = b''

base64_output = cm.convert_hex_to_base64(set1_01_input_data)

print(base64_output)

if base64_output == set1_01_expected_result:
    print("Success!")
else:
    print("Failed!")

# Test with Home-Brewed Base64 Decoder:
base64_output_home_brew = b''
base64_output_home_brew = cm.convert_hex_to_base64_homebrew(set1_01_input_data)

print(base64_output_home_brew)
if base64_output_home_brew == set1_01_expected_result:
    print("Success!")
    exit(0)
else:
    print("Failed! Home Brewed version")
    exit(-1)