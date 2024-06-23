def reverse_transform(encoded_flag):
    # 逆変換ステップ1: 36進数から文字列への変換
    parts = encoded_flag.split('_')
    decoded = ''.join([chr(int(c, 36) + 10) for c in parts])
    
    # 逆変換ステップ2: XOR操作
    xored = ''.join([chr(123 ^ ord(c)) for c in decoded])
    
    # 逆変換ステップ3: -3シフト操作
    shifted = ''.join([chr(ord(c) - 3) for c in xored])
    
    # 逆変換ステップ4: +12シフト操作
    final = ''.join([chr(ord(c) + 12) for c in shifted])
    
    return final

encoded_flag = "16_10_13_x_6t_4_1o_9_1j_7_9_1j_1o_3_6_c_1o_6r"
flag = reverse_transform(encoded_flag)
print("The correct flag is:", flag)