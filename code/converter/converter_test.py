#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        01-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
import unittest

from converter import Converter


class ConverterTest(unittest.TestCase):

    def setUp(self):
        # Arrange
        self._uut = Converter()

    # region Convert_Hex_bytes_to_Base64
    def test_ConvertHexToBase64_ValidInput_CorrectBase64Bytes(self):
        # Arrange
        test_string1 = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        expected_result = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

        # Act
        result = self._uut.convert_hex_to_base64(test_string1)

        # Assert
        self.assertEqual(result, expected_result)

    # endregion Convert_HEx_bytes_to_Base64

    # region Convert_string_to_Hex_bytes
    def test_ConvertStringToHex_ValidString_CorrectHexBytes(self):
        # Arrange
        test_string1 = 'test'
        expected_result = b'74657374'

        # Act
        result = self._uut.convert_string_to_hex(test_string1)

        # Assert
        self.assertEqual(result, expected_result)

    # endregion Convert_string_to_hex_bytes

    # region Convert_Hex_bytes_to_String

    def test_ConvertHexToString_ValidHexBytesWithHexPrefix_CorrectString(self):
        # Arrange
        test_bytes = b'0x74657374'
        expected_result = 'test'

        # Act
        result = self._uut.convert_hex_to_string(test_bytes)

        # Assert
        self.assertEqual(result, expected_result)

    def test_ConvertHexToString_ValidHexBytesWithoutHexPrefix_CorrectString(self):
        # Arrange
        test_bytes = b'74657374'
        expected_result = 'test'

        # Act
        result = self._uut.convert_hex_to_string(test_bytes)

        # Assert
        self.assertEqual(result, expected_result)

    # endregion Convert_Hex_bytes_to_String

    # region Convert_Hex_bytes_to_String_bytes

    def test_ConvertHexToStringBytes_ValidHexBytesWithoutHexPrefix_CorrectStringBytes(self):
        # Arrange
        test_bytes = b'7465737474657374'
        expected_result = b'testtest'

        # Act
        result = self._uut.convert_hex_to_string_bytes(test_bytes)

        # Assert
        self.assertEqual(result, expected_result)

    def test_ConvertHexToStringBytes_ValidHexBytesWithHexPrefix_CorrectStringBytes(self):
        # Arrange
        test_bytes = b'0x7465737474657374'
        expected_result = b'testtest'

        # Act
        result = self._uut.convert_hex_to_string_bytes(test_bytes)

        # Assert
        self.assertEqual(result, expected_result)

    # endregion Convert_Hex_bytes_to_String_bytes


if __name__ == '__main__':
    unittest.main()
