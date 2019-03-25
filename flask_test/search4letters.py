def search_for_letters(phrase: str, letters: str = 'aeiou') ->set:
    '''return any letters found in a supplied word.'''
    return set(letters).intersection(set(phrase))