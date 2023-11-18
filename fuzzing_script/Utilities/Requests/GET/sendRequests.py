<<<<<<< HEAD
import re
from itertools import zip_longest
from threading import Thread
from ...CheckRequests.check import tryExceptRequests
arrayOfThreads = []


def runCutDiccionary(n, iterable, padvalue='x'):
    return zip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

def targetFuzz(
    cutWordList: list,
    url: str,
    userAgent: list,
    delayParam: int,

    cookies: dict,
    headers: dict,

    hideHTTPCodes: str,
    avaliableHTTPCodes: str,
    hideCharacters: str,
    avaliableCharacters: str,

    skipSSL: bool,
    followRedirect: bool,
    httpProxies: list,
    httpsProxies: list,

    subDomain: bool,
    originalURL: str
):
    for i in cutWordList:
        if (subDomain):
            # Temp var
            x = i.rstrip()
            y = originalURL
            payload = re.sub("/kFuzz", f"{x}", y)
            
            tryExceptRequests(
                url=payload,
                hideHTTPCodes=hideHTTPCodes,
                avaliableHTTPCodes=avaliableHTTPCodes,
                hideCharacters=hideCharacters,
                avaliableCharacters=avaliableCharacters,
                delayParam=delayParam,
                cookies=cookies,
                headers=headers,
                skipSSL=skipSSL,
                userAgent=userAgent,
                followRedirect=followRedirect,
                httpProxies=httpProxies,
                httpsProxies=httpsProxies
            )
        
        else:
            if (i[0] != "/"):
                # Temp var
                payload = f"{url}/{i}".rstrip()

                tryExceptRequests(
                url=payload,
                hideHTTPCodes=hideHTTPCodes,
                avaliableHTTPCodes=avaliableHTTPCodes,
                hideCharacters=hideCharacters,
                avaliableCharacters=avaliableCharacters,
                delayParam=delayParam,
                cookies=cookies,
                headers=headers,
                skipSSL=skipSSL,
                userAgent=userAgent,
                followRedirect=followRedirect,
                httpProxies=httpProxies,
                httpsProxies=httpsProxies
            )

            else:
                # Temp var
                payload = f"{url}{i}".rstrip()

                tryExceptRequests(
                    url=payload,
                    hideHTTPCodes=hideHTTPCodes,
                    avaliableHTTPCodes=avaliableHTTPCodes,
                    hideCharacters=hideCharacters,
                    avaliableCharacters=avaliableCharacters,
                    delayParam=delayParam,
                    cookies=cookies,
                    headers=headers,
                    skipSSL=skipSSL,
                    userAgent=userAgent,
                    followRedirect=followRedirect,
                    httpProxies=httpProxies,
                    httpsProxies=httpsProxies
                )
            
def runFuzz(
    wordList: list,
    url: str,
    cookies: dict,
    headers: dict,

    skipSSL: bool,
    followRedirect: bool,
    subDomain: bool,
    httpProxies: list,
    httpsProxies: list,

    userAgent: list,
    threads: int,
    delayParam: int,

    hideHTTPCodes: str,
    avaliableHTTPCodes: str,
    avaliableCharacters: str,
    hideCharacters: str,
):
    # ----------------------------------------------------------------------------
    # Math to know Words x Thread
    math = round(len(wordList) / int(threads))

    # ----------------------------------------------------------------------------
    # Case 1: .htaccess || index.html
    originalURL = url
    url = re.sub("/kFuzz", "", url)

    # ----------------------------------------------------------------------------
    # hideHTTPCodes and avaliableHTTPCodes Array
    try:
        if (hideHTTPCodes != None):
            hideHTTPCodes = hideHTTPCodes.split(",")
        elif (avaliableHTTPCodes != None):
            avaliableHTTPCodes = avaliableHTTPCodes.split(",")
    except:
        pass

    try:
        if (avaliableCharacters != None):
            avaliableCharacters = avaliableCharacters.split(",")
        elif (hideCharacters != None):
            hideCharacters = hideCharacters.split(",")
    except:
        pass

    # This return segments of wordList, this divided wordList in few lists
    # This [lists] match with [threads]
    # FOR EXAMPLE: 15 [Threads] == 15 [List] (For list has... i dont know... 400 words?)
    for list in runCutDiccionary(math, wordList):
        try:
            t = Thread(target=targetFuzz,
                       args=(
                           list,
                           url,
                           userAgent,
                           delayParam,

                           cookies,
                           headers,

                           hideHTTPCodes,
                           avaliableHTTPCodes,
                           hideCharacters,
                           avaliableCharacters,

                           skipSSL,
                           followRedirect,
                           httpProxies,
                           httpsProxies,
                           subDomain,
                           originalURL
                       ))
            arrayOfThreads.append(t)
            t.start()

        except KeyboardInterrupt:
            print()
            print("[-] Saliendo...")

    return 0
=======
import re
from itertools import zip_longest
from threading import Thread
from ...CheckRequests.check import tryExceptRequests
arrayOfThreads = []


def runCutDiccionary(n, iterable, padvalue='x'):
    return zip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

def targetFuzz(
    cutWordList: list,
    url: str,
    userAgent: list,
    delayParam: int,

    cookies: dict,
    headers: dict,

    hideHTTPCodes: str,
    avaliableHTTPCodes: str,
    hideCharacters: str,
    avaliableCharacters: str,

    skipSSL: bool,
    followRedirect: bool,
    httpProxies: list,
    httpsProxies: list,

    subDomain: bool,
    originalURL: str
):
    for i in cutWordList:
        if (subDomain):
            # Temp var
            x = i.rstrip()
            y = originalURL
            payload = re.sub("/kFuzz", f"{x}", y)
            
            tryExceptRequests(
                url=payload,
                hideHTTPCodes=hideHTTPCodes,
                avaliableHTTPCodes=avaliableHTTPCodes,
                hideCharacters=hideCharacters,
                avaliableCharacters=avaliableCharacters,
                delayParam=delayParam,
                cookies=cookies,
                headers=headers,
                skipSSL=skipSSL,
                userAgent=userAgent,
                followRedirect=followRedirect,
                httpProxies=httpProxies,
                httpsProxies=httpsProxies
            )
        
        else:
            if (i[0] != "/"):
                # Temp var
                payload = f"{url}/{i}".rstrip()

                tryExceptRequests(
                url=payload,
                hideHTTPCodes=hideHTTPCodes,
                avaliableHTTPCodes=avaliableHTTPCodes,
                hideCharacters=hideCharacters,
                avaliableCharacters=avaliableCharacters,
                delayParam=delayParam,
                cookies=cookies,
                headers=headers,
                skipSSL=skipSSL,
                userAgent=userAgent,
                followRedirect=followRedirect,
                httpProxies=httpProxies,
                httpsProxies=httpsProxies
            )

            else:
                # Temp var
                payload = f"{url}{i}".rstrip()

                tryExceptRequests(
                    url=payload,
                    hideHTTPCodes=hideHTTPCodes,
                    avaliableHTTPCodes=avaliableHTTPCodes,
                    hideCharacters=hideCharacters,
                    avaliableCharacters=avaliableCharacters,
                    delayParam=delayParam,
                    cookies=cookies,
                    headers=headers,
                    skipSSL=skipSSL,
                    userAgent=userAgent,
                    followRedirect=followRedirect,
                    httpProxies=httpProxies,
                    httpsProxies=httpsProxies
                )
            
def runFuzz(
    wordList: list,
    url: str,
    cookies: dict,
    headers: dict,

    skipSSL: bool,
    followRedirect: bool,
    subDomain: bool,
    httpProxies: list,
    httpsProxies: list,

    userAgent: list,
    threads: int,
    delayParam: int,

    hideHTTPCodes: str,
    avaliableHTTPCodes: str,
    avaliableCharacters: str,
    hideCharacters: str,
):
    # ----------------------------------------------------------------------------
    # Math to know Words x Thread
    math = round(len(wordList) / int(threads))

    # ----------------------------------------------------------------------------
    # Case 1: .htaccess || index.html
    originalURL = url
    url = re.sub("/kFuzz", "", url)

    # ----------------------------------------------------------------------------
    # hideHTTPCodes and avaliableHTTPCodes Array
    try:
        if (hideHTTPCodes != None):
            hideHTTPCodes = hideHTTPCodes.split(",")
        elif (avaliableHTTPCodes != None):
            avaliableHTTPCodes = avaliableHTTPCodes.split(",")
    except:
        pass

    try:
        if (avaliableCharacters != None):
            avaliableCharacters = avaliableCharacters.split(",")
        elif (hideCharacters != None):
            hideCharacters = hideCharacters.split(",")
    except:
        pass

    # This return segments of wordList, this divided wordList in few lists
    # This [lists] match with [threads]
    # FOR EXAMPLE: 15 [Threads] == 15 [List] (For list has... i dont know... 400 words?)
    for list in runCutDiccionary(math, wordList):
        try:
            t = Thread(target=targetFuzz,
                       args=(
                           list,
                           url,
                           userAgent,
                           delayParam,

                           cookies,
                           headers,

                           hideHTTPCodes,
                           avaliableHTTPCodes,
                           hideCharacters,
                           avaliableCharacters,

                           skipSSL,
                           followRedirect,
                           httpProxies,
                           httpsProxies,
                           subDomain,
                           originalURL
                       ))
            arrayOfThreads.append(t)
            t.start()

        except KeyboardInterrupt:
            print()
            print("[-] Saliendo...")

    return 0
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
