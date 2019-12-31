def wordPattern(wordParrern,input):
    word = input.split(' ')
    if len(word) != len(wordParrern):
        return False
    hash={}
    used={}
    for i in range(len(wordParrern)):
        if wordParrern[i] in hash:
            if hash[wordParrern[i]] != word[i]:
                return False
            else:
                if word[i] in used:
                    return False
        hash[wordParrern[i]] = word[i]
        used[word[i]] = True
        print(hash)
        print(used)
    return True
put=input('enter: ')
word=['app','app','ban','ban']
print(wordPattern(word,put))