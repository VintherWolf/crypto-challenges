#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest

from .set_one import Converter
from .set_one_testdata import input_hex_string, expected_base64


class ConverterTest(unittest.TestCase):

    def setUp(self):
        # Arrange
        __nop = ''

    def test_fromHexbytesToBase64_CorrectOutput(self):
        # Arrange
        self._uut = Converter(input_hex_string)

        # Act
        self._uut.from_hexbytes_to_base64()

        # Assert
        self.assertEqual(self._uut.output_base64, expected_base64)


if __name__ == '__main__':
    unittest.main()
