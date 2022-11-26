def print_upper_words(words, must_start_with={'e'}):
    """ Convert words that start with the letter 'e' (default)
    accepts a Dict with letters and returns Upper case words that only
    have the letters specified in the Dict
    """
    for words in words:  # loop words list
        for char in must_start_with:  # loop must_start_with keys
            if char == words[0]:
                print(words.upper())


print('upper case words that start with "h" or "w"')
print_upper_words(['hello', 'world', 'everyone',
                   'loves', 'python'], {'h', 'w'})
print('\nupper case words that start with default value "e"')
print_upper_words(['hello', 'world', 'everyone', 'eats', 'elfs'])