print('\n**********************************')


def print_upper_words(words):
    """ Prints words in upper case on a seperate line
    expample ['hi','people'] ---->>>>
    HI
    PEOPLE
    """
    for word in words:
        print(word.upper())


print_upper_words(['hello', 'world', 'loving', 'python'])
print('\n**********************************')


def print_upper_words_starting_with_e(words):
    """ prints words that start with the letter 'e'
    upper cased and on a seperate line
    example ['elephant', 'eats', 'elfs', 'and', 'people']

    ELEPHANT
    EATS
    ELFS
    """
    for word in words:
        if word[0] == 'e':
            print(word.upper())


print_upper_words_starting_with_e(
    ['elephant', 'eats', 'elfs', 'and', 'people'])
print('\n**********************************')


def print_upper_words_that_match_dict(words, must_start_with):
    """ prints words that start with the keys in dict,
    upper cased and on a seperate line.
    example ['elephant', 'eats', 'elfs', 'and', 'people']

    ELEPHANT
    EATS
    ELFS
    PEOPLE
    """
    for words in words:  # loop words list
        for char in must_start_with:  # loop must_start_with keys
            if char == words[0]:
                print(words.upper())


print_upper_words_that_match_dict(
    ['elephant', 'eats', 'elfs', 'and', 'people'], {'e', 'p'})
print('\n**********************************')
