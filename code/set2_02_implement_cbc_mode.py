#!/usr/bin/env python
# CBC Mode
from base64 import b64decode
from Crypto.Cipher import AES

from cryptomodule import CryptoModule
from set2_01_pkcs7_padding import set_pkcs7_padding


cm = CryptoModule()
output = ''
key = b'YELLOW SUBMARINE'
iv = b'\x00' * AES.block_size
ciphers = cm.read_file_as_bytes('set2_02_ciphers.txt')
ciphers = cm.convert_base64_to_bytes(ciphers)

text = cm.aes_cbc_decrypt(ciphers, key, iv).decode().rstrip()

# Check that the encryption/decryption methods work fine with a custom input
custom_input = b'Trying to decrypt something else to see if it works.'
assert cm.aes_cbc_decrypt(aes_cbc_encrypt(
    custom_input, key, iv), key, iv) == custom_input
