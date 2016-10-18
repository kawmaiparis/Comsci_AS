def monkeytyping(words):
    newword = ""
    message = []
    for letter in range(len(words)):
        if words[letter] == words[letter].upper():
            newword = newword + words[letter]
    print(newword)
        


