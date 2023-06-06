import string


def caesar_cipher(text, shift, decrypt=False):
    """
    Caesar cipher implementation in Python.
    """
    # Create input and output character maps
    alphabet = string.ascii_lowercase
    if decrypt:
        shift = -shift
    input_map = str.maketrans(alphabet, alphabet[shift:] + alphabet[:shift])
    output_map = str.maketrans(alphabet[shift:] + alphabet[:shift], alphabet)

    # Transform input text based on mode
    if decrypt:
        return text.translate(output_map)
    else:
        return text.translate(input_map)
