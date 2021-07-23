#!/usr/bin/env python
# PKCS7 Padding
import unittest

from set2_01_pkcs7_padding import set_pkcs7_padding


class CbcModeTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_implementCBCMode_CorrectPlainText(self):
        # Arrange
        input_text = b'YELLOW RED'
        six_bytes_padding = b'\x04'*6
        expected_result = input_text + six_bytes_padding

        # Act
        result = set_pkcs7_padding(input_text, 8)
        padding = hex(4)

        # Assert
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
