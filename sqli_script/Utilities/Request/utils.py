from simple_colors import *

def clean_wordlist(wordlist: list):
    clean_list = []

    for word in wordlist:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "

        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)

    return clean_list

def extract_wordlist(soup):
    wordlist = []

    for each_text in soup.findAll('div'):
        content = each_text.text
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)

    wordlist = clean_wordlist(wordlist)

    return wordlist

def check_response(
    responseStatus: int,
    responseLenght: int,
    hideResponse: int,
    hideLenght: int,
    payload: str
):
    # Print all
    if hideResponse == "" and hideLenght == "":
        print( f"Response: {responseStatus}, Lenght: {responseLenght}, Payload: {payload}" )
        
    # Avoid errors
    elif hideResponse != "" and hideLenght != "":
        exit(f"{red('[-] ERROR:')} {yellow('No is possible work with [StatusCode] and [HideLenght] in the same attack')}")
        
    # Hide response status
    elif hideResponse != "":
        if str(responseStatus) == str(hideResponse):
            pass
        else:
            print( f"Response: {responseStatus}, Lenght: {responseLenght}, Payload: {payload}" )
            exit(1)
    
    # Hide lenght status
    elif hideLenght != "":
        if str(responseLenght) == str(hideLenght):
            pass
        else:
            print( f"Response: {responseStatus}, Lenght: {responseLenght}, Payload: {payload}" )
            exit(1)