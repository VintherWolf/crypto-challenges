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

######
# 03
######
xored_string_unknown_key = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
expected_plain_output = 'the kid don\'t play'
testoutput = 'readable string'

######
# 05
######
plain_text = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

ecrypted_string = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
