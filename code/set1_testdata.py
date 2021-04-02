# ====================================
# 01    Convert Hex to Base64
# ====================================
# Input
set1_01_input_data = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
# Expected output
set1_01_expected_result = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

# ====================================
# 02    Fixed XOR (Equal Length Inputs)
# ====================================
# Input
set1_02_input_data1 = b'1c0111001f010100061a024b53535009181c'
set1_02_input_data2 = b'686974207468652062756c6c277320657965'
# Expected output
set1_02_expected_result = b'746865206b696420646f6e277420706c6179'

# ====================================
# 03    Single Byte XOR Cipher
# ====================================
# Input
set1_03_input_data = bytes.fromhex(
    '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
# Expected output
set1_03_expected_result = 'Cooking MC\'s like a pound of bacon'

# ====================================
# 04    Detect Single Byte XOR Key
# ====================================
# Input
set1_04_input_data = '0e3647e8592d35514a081243582536ed3de6734059001e3f535ce6271032\n334b041de124f73c18011a50e608097ac308ecee501337ec3e100854201d\n1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736\n40e127f51c10031d0133590b1e490f3514e05a54143d08222c2a4071e351\n'.splitlines()
# Expected output
set1_04_expected_result = 'Now that the party is jumping'

# ====================================
# 05
# ====================================
# Input
set1_05_input_data = ''
# Expected output
set1_05_expected_result = ''
