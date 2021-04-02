#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        02-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
from cryptomodule import CryptoModule
from set1_testdata import set1_03_input_data, set1_03_expected_result


cm = CryptoModule()


output = cm.singlechar_brute_force(set1_03_input_data)

for idx, line in enumerate(output):

    print(line)

if output[0][3] == set1_03_expected_result:
    print("Success!")
    exit(0)
else:
    exit(-1)
