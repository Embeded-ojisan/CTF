import sys

sys.setrecursionlimit(10000000)

def transform_input(input_str):
    # First transformation
    step1 = ''.join(chr(ord(c) + 12) for c in input_str)
    # Second transformation
    step2 = ''.join(chr(ord(c) - 3) for c in step1)
    # Third transformation
    step3 = ''.join(chr(123 ^ ord(c)) for c in step2)
    return step3

def reverse_transform_input(output_str):
    # Third transformation (reverse XOR with 123)
    step2 = ''.join(chr(123 ^ ord(c)) for c in output_str)
    # Second transformation (reverse -3, i.e., +3)
    step1 = ''.join(chr(ord(c) + 3) for c in step2)
    # First transformation (reverse +12, i.e., -12)
    input_str = ''.join(chr(ord(c) - 12) for c in step1)
    return input_str

def decode(encoded_str):
    return ''.join(chr(int(c, 36) + 10) for c in encoded_str.split('_'))

def main():
    encoded_str = '16_10_13_x_6t_4_1o_9_1j_7_9_1j_1o_3_6_c_1o_6r'
    correct_decoded_str = decode(encoded_str)

    user_input = input('Enter the flag: ')
    transformed_input = transform_input(user_input)

    print(correct_decoded_str)
    a = reverse_transform_input(correct_decoded_str)
    print(a)

    if transformed_input == correct_decoded_str:
        print('Correct FLAG!')
    else:
        print('Incorrect')

if __name__ == '__main__':
    main()
