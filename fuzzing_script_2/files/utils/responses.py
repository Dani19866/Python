<<<<<<< HEAD
def clean_wordlist(wordlist: list):
    clean_list = []

    for word in wordlist:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "

        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)

    return clean_list

def calcule_lenght(soup):
    wordlist = []

    for each_text in soup.findAll('div'):
        content = each_text.text
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)

    wordlist = clean_wordlist(wordlist)

=======
def clean_wordlist(wordlist: list):
    clean_list = []

    for word in wordlist:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "

        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)

    return clean_list

def calcule_lenght(soup):
    wordlist = []

    for each_text in soup.findAll('div'):
        content = each_text.text
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)

    wordlist = clean_wordlist(wordlist)

>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
    return wordlist