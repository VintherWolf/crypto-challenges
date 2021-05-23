#!/usr/bin/env python
# PKCS7 Padding


def set_pkcs7_padding(text, block_size):
    output = ''
    padding = bytes.fromhex('04')

    padding_len = evaluate_padding_need(text, block_size)
    padding *= padding_len
    text = text + padding

    return text


def evaluate_padding_need(text, block_size):

    padding_len = 0
    text_len = len(text)

    while (text_len % block_size != 0):
        text_len += 1
        padding_len += 1

    return padding_len
