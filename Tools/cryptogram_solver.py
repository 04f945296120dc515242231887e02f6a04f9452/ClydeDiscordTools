import itertools

def solve_cryptogram(cryptogram, word_list):
    """
    Solve a cryptogram by mapping each unique letter to a unique digit.
    """
    # Create a set of unique letters in the cryptogram
    letters = set(cryptogram)
    
    # Create a list of all possible digit assignments
    digit_assignments = itertools.permutations(range(10), len(letters))
    
    # Iterate over possible digit assignments and check if they produce valid words
    for digits in digit_assignments:
        digit_map = str.maketrans(''.join(letters), ''.join(str(d) for d in digits))
        candidate_words = [word.translate(digit_map) for word in word_list]
        if all(word.isnumeric() or word in word_list for word in candidate_words):
            return {letter: digit for letter, digit in zip(letters, digits)}
