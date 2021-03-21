######
# 01
######

# Raw hex string
input_hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

# Base64 output in bytes
expected_base64 = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

######
# 02
######

# String input
input_string = b'1c0111001f010100061a024b53535009181c'

# String to XOR against
compare_string = b'686974207468652062756c6c277320657965'

# Expected output after XOR
expected_output = b'746865206b696420646f6e277420706c6179'
