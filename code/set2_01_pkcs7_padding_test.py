#!/usr/bin/env python
# PKCS7 Padding
import unittest

from s201_pkcs7_padding import set_pkcs7_padding


class PaddingTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_setPkcs7Padding_TenBytesPlainText_IsPaddedToSixteen(self):
        # Arrange
        input_text = b'YELLOW RED'
        six_bytes_padding = b'\x04'*6
        expected_result = input_text + six_bytes_padding

        # Act
        result = set_pkcs7_padding(input_text, 8)
        padding = hex(4)

        # Assert
        self.assertEqual(result, expected_result)

    def test_setPkcs7Padding_SeventeenBytesPlainText_SevenBytesPadding(self):
        # Arrange
        input_text = b'SIXTEEN BYTE KEY+'
        seven_bytes_padding = b'\x04'*7
        expected_result = input_text + seven_bytes_padding

        # Act
        result = set_pkcs7_padding(input_text, 8)
        padding = hex(4)

        # Assert
        self.assertEqual(result, expected_result)

    def test_setPkcs7Padding_SixteenBytesPlainText_NoPadding(self):
        # Arrange
        input_text = b'SIXTEEN BYTE KEY'
        expected_result = input_text

        # Act
        result = set_pkcs7_padding(input_text, 8)
        padding = hex(4)

        # Assert
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
