#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        02-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
from cryptomodule import CryptoModule
from set1_testdata import set1_02_input_data1, set1_02_input_data2, set1_02_expected_result


cm = CryptoModule()

output = b''
output = cm.equal_length_inputs_xor(set1_02_input_data1, set1_02_input_data2)

print(output)

if output == set1_02_expected_result:
    print("Success!")
    exit(0)
else:
    exit(-1)
