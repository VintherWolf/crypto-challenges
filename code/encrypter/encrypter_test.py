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


class EncrypterTest(unittest.TestCase):

    def setUp(self):
        # Arrange
        self._uut = Encrypter()

    def test_RepeatingKeyXOrHex_ValidInput_CorrectCipherText(self):
        # Arrange
        test_string = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
        test_key = b'ICE'
        result = ''
        expected_result = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
        # Act
        result = self._uut.encrypt_repeating_key_xor_hex(test_string, test_key)

        # Assert
        self.assertEqual(result, expected_result)

    def test_RepeatingKeyXOrPlain_ValidInput_CorrectCipherText(self):
        # Arrange
        test_string = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
        test_key = b'ICE'
        result = ''
        expected_result = b'\x0b67\'*+.cb,.ii*#i:*<c$ -b=c4<*&"c$\'\'e\'*(+/ C\ne.,e*1$3:e>+ \'c\x0ci+ (1e(c&0.\'(/'
        # Act
        result = self._uut.encrypt_repeating_key_xor_plain(
            test_string, test_key)
        print(result)
        # Assert
        self.assertEqual(result, expected_result)

# region AES_ECB_MODE

    def test_RepeatingKeyXOrPlain_ValidInput_CorrectCipherText(self):
        # Arrange
        test_data1 = b'testTESTtestTEST'
        test_key = b'YELLOW SUBMARINE'
        result = b''
        expected_result = bytes.fromhex('D5119B1375DDCFF464479495F34830D660FA36707E45F499DBA0F25B922301A5')
        
        # Act
        result = self._uut.encrypt_aes_128b_ecb_mode(test_data1, test_key)

        # Assert
        self.assertEqual(result, expected_result)

# endregion AES_ECB_MODE
if __name__ == '__main__':
    unittest.main()
