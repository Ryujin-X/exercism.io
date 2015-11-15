import string


cipher = str.maketrans(string.ascii_lowercase[::-1], string.ascii_lowercase, string.punctuation + string.whitespace)

def decode(input_str):
    return ''.join(input_str.lower().translate(cipher))

def encode(input_str):
    encoded_str = decode(input_str)
    return ' '.join([encoded_str[i:i+5] for i in range(0, len(encoded_str), 5)])
