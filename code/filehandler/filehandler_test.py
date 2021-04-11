#!/usr/bin/env python
'''
    Author:         Daniel K. Vinther Wolf
    Created:        01-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
import unittest

from filehandler import FileHandler


class FileHandlerTest(unittest.TestCase):

    def setUp(self):
        # Arrange
        self._uut = FileHandler()

# region ReadBytesFromHexFile
    def test_ReadFileasHexbytes_ValidInput_CorrectHexValues(self):
        # Arrange
        filename = 'filehandler\\01_Hexciphers.txt'
        result = ''
        expected_result = [
        b'\xd5\x11\x9b\x13u\xdd\xcf\xf4dG\x94\x95\xf3H0\xd6`\xfa6p~E\xf4\x99\xdb\xa0\xf2[\x92#\x01\xa5', 
        b'\xd5\x11\x9b\x13u\xdd\xcf\xf4dG\x94\x95\xf3H0\xd6`\xfa6p~E\xf4\x99\xdb\xa0\xf2[\x92#\x01\xa5', 
        b'\xd6\x11\x9b\x13u\xdd\xcf\xf4dG\x94\x95\xf3H0\xd6`\xfa6p~E\xf4\x99\xdb\xa0\xf2[\x92#\x01\xa5',
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        b'\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11',
        b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',
        ]
        
        # Act
        result = self._uut.read_file_as_hexbytes(filename)

        # Assert
        self.assertEqual(result, expected_result)

# endregion ReadBytesFromHexFile

if __name__ == '__main__':
    unittest.main()