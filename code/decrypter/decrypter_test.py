#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        01-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
import unittest

from decrypter import Decrypter


class DecrypterTest(unittest.TestCase):

    def setUp(self):
        # Arrange
        self._uut = Decrypter()

    # region ComputeHammingDistance
    def test_ComputeHammingDistance_ValidInput_DistanceIsCorrectValue(self):
        # Arrange

        test_string1 = b'this is a test'
        test_string2 = b'wokka wokka!!!'
        distance = 0

        # Act
        distance = self._uut.compute_hamming_distance(
            test_string1, test_string2)

        # Assert
        self.assertEqual(distance, 37)

    def test_ComputeHammingDistance_LengthIsNotEqual_DistanceIsMinusOne(self):
        # Arrange
        test_string1 = b'this is a test'
        test_string2 = b'wokka wokka!!!wokka wokka!!!'
        distance = 0

        # Act
        distance = self._uut.compute_hamming_distance(
            test_string1, test_string2)

        # Assert
        self.assertEqual(distance, -1)
    # endregion ComputeHammingDistance

    # region SingleCharBruteForce

    def test_SingleByteXOr_ValidInput_XOrOutputIsCorrect(self):
        # Arrange
        # test_data found with help from https://www.dcode.fr/xor-cipher
        test_data = b',=+,'
        test_key = b'X'
        expected_xor_output = b'test'
        result = b''

        # Act
        result = self._uut.singlebyte_xor(test_data, test_key)

        # Assert
        self.assertEqual(result, expected_xor_output)

    def test_RateText_ValidText_RatingIsCorrect(self):
        # Arrange
        test_text = b'this text is awesome, that\'s what she said'
        test_text2 = 'THIS TEXT IS AWESOME, ThAT\'S WhAt sHe sAId'
        expected_rating = 4.49
        result = 0

        # Act
        result = self._uut.rate_text(test_text)
        result2 = self._uut.rate_text(test_text2)

        # Assert
        self.assertEqual(result, expected_rating)
        self.assertEqual(result2, expected_rating)

    def test_RateText_AllCommonWords_RatingIsCorrect(self):
        # Arrange

        test_text = b'THISandTHAThaveTHE'
        expected_rating = 4.71
        result = 0

        # Act
        result = self._uut.rate_text(test_text)

        # Assert
        self.assertEqual(result, expected_rating)



    # region EqualLengthXOr
    def test_EqualLengthInputXor_ValidInput_XOrOutputIsCorrect(self):
        # Arrange
        test_data1 = b'1c0111001f010100061a024b53535009181c'
        test_data2 = b'686974207468652062756c6c277320657965'
        expected_xor_output = b'746865206b696420646f6e277420706c6179'
        result = b''

        # Act
        result = self._uut.equal_length_inputs_xor(test_data1, test_data2)

        # Assert
        self.assertEqual(result, expected_xor_output)
    # endregion EqualLengthXOr


if __name__ == '__main__':
    unittest.main()
