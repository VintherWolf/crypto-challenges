#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        20-03-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''

from __future__ import absolute_import

import unittest

from .decrypter import Decrypter
from .set1_06_converter import Converter
from .set1_06_testdata import input_hex_string, expected_base64
from .set1_06_testdata import input_string, compare_string, expected_output
from .set1_06_testdata import xored_string_unknown_key, expected_plain_output, testoutput
from .set1_06_testdata import plain_text, ecrypted_string


class ConverterTest(unittest.TestCase):

    def setUp(self):
        # Arrange
        pass  # nop

    def test_ComputeHammingDistance_DistanceIsCorrectValue(self):
        # Arrange
        self._uut = Decrypter()
        test_string1 = 'this is a test'
        test_string2 = 'wokka wokka!!!'

        # Act
        self._uut.compute_hamming_distance(test_string1, test_string2)

        # Assert
        self.assertEqual(self._uut.hamming_distance,
                         37)


if __name__ == '__main__':
    unittest.main()
