#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest

from .set1_06_converter import Converter
from .set1_06_testdata import input_hex_string, expected_base64
from .set1_06_testdata import input_string, compare_string, expected_output
from .set1_06_testdata import xored_string_unknown_key, expected_plain_output, testoutput
from .set1_06_testdata import plain_text, ecrypted_string


class ConverterTest(unittest.TestCase):

    def setUp(self):
        # Arrange
        pass  # nop

    def test_EncryptText_OutputIsCorrectEncryptionString_(self):
        # Arrange
        self._uut = Converter()

        # Act
        self._uut.encrypt_with_repeating_key_xor(plain_text, "ICE")

        # Assert
        self.assertEqual(self._uut.output_xor,
                         ecrypted_string)


if __name__ == '__main__':
    unittest.main()
