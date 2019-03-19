def search_for_letters(word: str, letters: str) ->set:
    '''return any letters found in a supplied word.'''
    return set(letters).intersection(set(word))