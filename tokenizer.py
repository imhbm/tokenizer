def convert_chars_to_token(all_characters):
    char_to_ascii = []
    for char in all_characters:
        ascii_value = ord(char)
        char_to_ascii.append(ascii_value)
    return char_to_ascii

def decode_token(ascii_values):
    decoded_chars = []
    for index in ascii_values:
        character = chr(index)
        decoded_chars.append(character)
    decoded_string = ''.join(decoded_chars)
    return decoded_string

sample_text = "Hello, chai and code!"

encoded_indices = convert_chars_to_token(sample_text)
print(f"Encoded text '{sample_text}' to indices: {encoded_indices}")

decoded_text = decode_token(encoded_indices)
print(f"Decoded indices back to text: '{decoded_text}'")

