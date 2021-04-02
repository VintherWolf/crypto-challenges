#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        01-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
import unittest

from cryptomodule import CryptoModule
from set1_testdata import set1_04_input_data


class CryptoModuleTest(unittest.TestCase):

    def setUp(self):
        # Arrange
        self._sut = CryptoModule()

# region SingleCharBruteForce
    def test_SingleCharBruteForxe_ValidCipherText_DecryptsToCorrectPlainText(self):
        # Arrange

        test_cipher_text = bytes.fromhex(
            '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
        expected_plain_text = 'Cooking MC\'s like a pound of bacon'
        result = []

        # Act
        result = self._sut.singlechar_brute_force(test_cipher_text)

        # Assert
        self.assertEqual(result[0][3], expected_plain_text)
# endregion SingleCharBruteForce

# region DetectEncryptionBySingleByteBruteForce
    def test_DetectSingleByte_ValidCipherText_DecryptsToCorrectPlainText(self):
        # Arrange
        expected_plain_text = 'Cooking MC\'s like a pound of bacon'
        result = []

        # Act
        result = self._sut.detect_encryption_by_singlechar_brute_force(
            set1_04_input_data)

        # Assert
        # Result contains [0][0] = Key, [0][1] Rating and [0][2] = Best Plain Text
        self.assertEqual(result[0][2], expected_plain_text)

    def test_DetectSingleByte_LoadValidCipherTextFromFile_DecryptsToCorrectPlainText(self):
        # Arrange
        test_cipher_text = b''
        expected_plain_text = 'Now that the party is jumping'
        result = []

        # Act
        test_cipher_text = self._sut.load_cipher_text_from_file(
            'set1_04_cipher.txt')

        result = self._sut.detect_encryption_by_singlechar_brute_force(
            test_cipher_text)

        # Assert
        self.assertEqual(result[0][2], expected_plain_text)

# endregion DetectEncryptionBySingleByteBruteForce


if __name__ == '__main__':
    unittest.main()
