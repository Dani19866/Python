<<<<<<< HEAD
import Modules.Module_Prints.Results.results as console

def defaultProcess(
        status_Code,
        url,
        words_len
):
    console.printResults(url, status_Code, words_len)
    return 0


def analyzeStatusCode(
    hideHTTPCodes,
    avaliableHTTPCodes,
    statusCode,
    
    words_len,
    url
):
    # Hidden HTTP Codes param
    if (hideHTTPCodes != None):
        if (str(statusCode) in hideHTTPCodes):
            pass
        else:
            console.printResults(url, statusCode, words_len)

    # Avaliable HTTP Codes param
    elif (avaliableHTTPCodes != None):
        if (str(statusCode) in avaliableHTTPCodes):
            console.printResults(url, statusCode, words_len)


def analyzeWords(
    avaliableCharacters,
    hideCharacters,
    words_len,
    
    url,
    status_code
):
    # Hidden HTTP Codes param
    if (hideCharacters != None):
        if (str(words_len) in hideCharacters):
            pass
        else:
            console.printResults(url, status_code, words_len)

    # Avaliable HTTP Codes param
    elif (avaliableCharacters != None):
        if (str(words_len) in avaliableCharacters):
            console.printResults(url, status_code, words_len)
=======
import Modules.Module_Prints.Results.results as console

def defaultProcess(
        status_Code,
        url,
        words_len
):
    console.printResults(url, status_Code, words_len)
    return 0


def analyzeStatusCode(
    hideHTTPCodes,
    avaliableHTTPCodes,
    statusCode,
    
    words_len,
    url
):
    # Hidden HTTP Codes param
    if (hideHTTPCodes != None):
        if (str(statusCode) in hideHTTPCodes):
            pass
        else:
            console.printResults(url, statusCode, words_len)

    # Avaliable HTTP Codes param
    elif (avaliableHTTPCodes != None):
        if (str(statusCode) in avaliableHTTPCodes):
            console.printResults(url, statusCode, words_len)


def analyzeWords(
    avaliableCharacters,
    hideCharacters,
    words_len,
    
    url,
    status_code
):
    # Hidden HTTP Codes param
    if (hideCharacters != None):
        if (str(words_len) in hideCharacters):
            pass
        else:
            console.printResults(url, status_code, words_len)

    # Avaliable HTTP Codes param
    elif (avaliableCharacters != None):
        if (str(words_len) in avaliableCharacters):
            console.printResults(url, status_code, words_len)
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
