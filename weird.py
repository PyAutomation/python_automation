def to_weird(text):
    words = []
    for word in text.split():
        new_word = ''
        counter = 0
        for letter in word:
            if counter % 2 == 0:
                new_word += letter.upper()
            else:
                new_word += letter.lower()
            counter += 1
        words.append(new_word)
    return ' '.join(words)


def autocomplete(string, *args):
    dictionaries = []
    search_word = ''
    for letter in string:
        if letter.isalpha():
            search_word += letter
    if search_word:
        for dictionary in args:
            new_dictionary = []
            for word in dictionary:
                if search_word.lower() == word[:len(search_word)].lower():
                    new_dictionary.append(word)
                    if len(new_dictionary) == 5:
                        break
            dictionaries.append(new_dictionary)
    else:
        print('Wrong input string!')
    if len(dictionaries) == 1:
        return dictionaries[0]
    else:
        return dictionaries