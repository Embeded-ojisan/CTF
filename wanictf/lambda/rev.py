def decode_flag():
    input_str = '16_10_13_x_6t_4_1o_9_1j_7_9_1j_1o_3_6_c_1o_6r'
    parts = input_str.split('_')
    decoded_chars = [chr(int(part, 36) + 10) for part in parts]
    decoded_str = ''.join(decoded_chars)
    return decoded_str

decoded_flag = decode_flag()
print(decoded_flag)