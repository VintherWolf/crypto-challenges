#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        01-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
import unittest

from encrypter import Encrypter


class ConverterTest(unittest.TestCase):

    def setUp(self):
        # Arrange
        self._uut = Encrypter()

    def test_RepeatingKeyXOr_ValidInput_CorrectCipherText(self):
        # Arrange
        test_string = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
        test_key = 'ICE'
        result = ''
        expected_result = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
        # Act
        result = self._uut.encrypt_xor_repeating_key(test_string, test_key)

        # Assert
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
