#!/usr/bin/env python
'''
    Author:        Daniel K. Vinther Wolf
    Created:       01-04-2021
    Description:
    Dependencies:
    Pre-Requisites:
'''
from base64 import b64encode, b64decode
from string import ascii_uppercase, ascii_lowercase, digits

class Converter(object):

    def __init__(self):
        pass

    # ==========================================
    # Hex Bytes as Input, Methods
    # ==========================================

    def convert_hex_to_base64(self, data):
        """
        Convert hex formated bytes to base64 encoding
        """
        data = self.convert_hex_bytes_to_string(data)
        return b64encode(data)

    def convert_hex_to_base64_homebrew(self, data):

        try:
            data = self.convert_hex_bytes_to_string(data)
        except:
            print("Input was not Hex-decimal. Converts as bytes")
            pass
        pad = '='
        sextets = 0b000000
        base64_output = ''

        # | 8 bits    | 8 bits   | 8 bits     | <- Input
        # | 6 bits | 6 bits | 6 bits | 6 bits | <- B64 Output
        #   Pos 1    Pos 2    Pos 3    Pos 4
        position = 0
        from_pos1 = 0b0
        from_pos2 = 0b0
        from_pos3 = 0b0

        padding = self.is_padding_needed(data)

        for byte in data:
                       
            position += 1
        
            if position == 1:
            # First sextet
                sextet = (byte >> 2)
                base64_output += self.base64_table[sextet]
                from_pos1 = (byte & 0b00000011)
                continue
            
            elif position == 2:
            # Second sextet
                sextet = (from_pos1 << 4)
                sextet |= (byte >> 4)
                base64_output += self.base64_table[sextet]

                from_pos2 = (byte & 0b00001111)
                continue

            elif position == 3:
                # Third and Fourth sextet
                sextet = (from_pos2 << 2) 
                sextet |= (byte >> 6)
                base64_output += self.base64_table[sextet]

                from_pos3 = (byte & 0b00111111)

                # Fourth:
                sextet = from_pos3
                base64_output += self.base64_table[sextet]
                position = 0
                continue
        
        if position == 2:
                # Third sextet and no more Bytes to convert
                sextet = (from_pos2 << 2) 
                sextet |= (0b00000000)
                base64_output += self.base64_table[sextet]
        
        if position == 1:
            # Second sextet and no more Bytes to convert
                sextet = (from_pos1 << 4)
                sextet |= (0b00000000)
                base64_output += self.base64_table[sextet]
        
        base64_output += (padding * pad)

        return base64_output.encode()





        

    def is_padding_needed(self, data):
        
        pad = b'='
        padding = 0

        if type(data) is str:
            data = data.encode()
        check_data = data
        # Base64 needs to be 6bits x K, where K is 4 * N, and N is 1 to "infinite"
        # Check if input which is in 8bit per char
        # will need padding to fit into 6bits x K
        while (len(check_data)*8) % 6 != 0:
            check_data += pad
            padding += 1

        return padding

    def set_padding(self, output, padding):
        pad = b'='
        # Base64 needs to be 6bits x K, where K is 4 * N, and N is 1 to "infinite"
        # Check if input which is in 8bit per char
        # will need padding to fit into 6bits x K
        while (len(output)*8) % 6 != 0:
            output += pad
    
        return output

    def convert_hex_to_string(self, data):
        """
        Convert hex formated bytes to string
        """
        output = self.__remove_hex_prefix_if_present(data)
        output = output.decode()
        return bytes.fromhex(output).decode()

    def convert_hex_bytes_to_string(self, data):
        """
        Convert hex formated bytes to string
        """
        output = self.__remove_hex_prefix_if_present(data)
        output = output.decode()
        return bytes.fromhex(output)

    def convert_hex_to_string_bytes(self, data):
        """
        Convert hex formated bytes to string
        """
        output = self.__remove_hex_prefix_if_present(data)
        output = output.decode()
        return bytes.fromhex(output)

    # ==========================================
    # String as Input, Methods
    # ==========================================

    def convert_string_to_hex(self, string):
        """
        Convert string to hex formated bytes
        """
        output = ''

        for char in string:
            output += hex(ord(char))[2:]

        return output.encode()

    # ==========================================
    # Pretty Print, Methods
    # ==========================================

    def convert_bytes_to_pretty_string_output(self, data):
        return data.decode().rstrip()
    
    def convert_bytes_to_pretty_print(self, data):
        print(data.decode().rstrip())

    # ==========================================
    # Base64 as Input, Methods
    # ==========================================

    def convert_base64_to_bytes(self, b64):
        return b64decode(b64)

    # ==========================================
    # Aggregate Methods
    # ==========================================

    def __remove_hex_prefix_if_present(self, data):
        """
        Remove "0x" prefix if present
        """
        if b'0x' in data[:2]:
            return data[2:]
        else:
            return data

    # ==========================================
    # Resources
    # ==========================================

    #base64_table = str(ascii_uppercase + ascii_lowercase + digits + '+/').encode()

    base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk" \
                     "lmnopqrstuvwxyz0123456789+/"