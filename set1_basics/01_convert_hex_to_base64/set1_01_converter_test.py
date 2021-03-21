#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest

from .set1_01_converter import Converter
from .set1_01_testdata import input_hex_string, expected_base64


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


if __name__ == '__main__':
    unittest.main()
