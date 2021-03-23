#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest

from .set1_04_converter import Converter
from .set1_04_testdata import input_hex_string, expected_base64
from .set1_04_testdata import input_string, compare_string, expected_output
from .set1_04_testdata import xored_string_unknown_key, expected_plain_output, testoutput


class ConverterTest(unittest.TestCase):

    def setUp(self):
        # Arrange
        pass  # nop

    def test_fromHexbytesToBase64_CorrectOutput(self):
        # Arrange
        self._uut = Converter(input_hex_string)

        # Act
        self._uut.from_hexbytes_to_base64()

        # Assert
        self.assertEqual(self._uut.output_base64, expected_base64)

    def test_fixedXor_CorrectOutput(self):
        # Arrange
        self._uut = Converter()

        # Act
        self._uut.produce_xor(input_string, compare_string)

        # Assert
        self.assertEqual(self._uut.output_xor, expected_output)

    def test_DecodeXorHexEncodedOutput_OutputIsCorrectPlainText(self):
        # Arrange
        self._uut = Converter()
        try_key = b'a'
        # Act
        self._uut.produce_xor(input_string, compare_string)

        # Assert
        self.assertEqual(self._uut.output_plain, expected_plain_output)

    def test_DecodeXorHexEncodedOutput_OutputIsPlainText(self):
        # Arrange
        self._uut = Converter(xored_string_unknown_key)

        # Act
        self._uut.atoz_singlechar_brute_force(self._uut.bytes_s_hex)

        # Assert
        counter = 0
        while True:

            if self._uut.output_plain == testoutput:
                print("cool")
            else:
                counter += 1

            if counter > 4000:
                break

        self.assertEqual(chr(self._uut.best_rated_key), 'X')
        self.assertEqual(self._uut.best_rated_plain_text,
                         'Cooking MC\'s like a pound of bacon')

    def test_DecodeCipherTextsFromFile_OutputIsPlainText(self):
        # Arrange
        self._uut = Converter()

        # Act
        self._uut.atoz_singlechar_brute_force_text_file()

        # Assert

        self.assertEqual(self._uut.best_rated_plain_text,
                         'Now that the party is jumping')
        self.assertEqual(self._uut.best_rated_key,
                         53)


if __name__ == '__main__':
    unittest.main()
