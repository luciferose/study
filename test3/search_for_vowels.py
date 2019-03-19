def search_for_vowels(word: str) ->set:
    '''return any vowels found in a supplied word.'''
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search_for_letters(word: str, letters: str) ->set:
    '''return any letters found in a supplied word.'''
    return set(letters).intersection(set(word))
