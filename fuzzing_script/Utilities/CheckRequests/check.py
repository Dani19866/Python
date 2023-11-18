<<<<<<< HEAD
import random
import requests
import Modules.Module_FilterValues.filter as checkStatus
import time
import re
from bs4 import BeautifulSoup
requests.packages.urllib3.disable_warnings()

def sendR(
    url: str,

    cookies: dict,
    headers: dict,

    skipSSL: bool,
    followRedirect: bool,
    httpProxies: list,
    httpsProxies: list
):
    if ( len( httpProxies ) > 0 ):
        package = requests.get(
            url=url,
            timeout=20,
            headers=headers,
            cookies=cookies,
            verify=skipSSL,
            allow_redirects=followRedirect,
            proxies={
                "http": httpProxies[random.randint(0, len(httpProxies) - 1)],
                "https": httpsProxies[random.randint(0, len(httpsProxies) - 1)]
            }
        )
        
        return package

    else:
        package = requests.get(
            url=url,
            timeout=20,
            headers=headers,
            cookies=cookies,
            verify=skipSSL,
            allow_redirects=followRedirect
        )
        
        return package


def delay(param: float):
    time.sleep(float(param))


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


def tryExceptRequests(
    url: str,
    delayParam: float,

    cookies: dict,
    headers: dict,
    userAgent: list,

    hideHTTPCodes: list,
    avaliableHTTPCodes: list,
    avaliableCharacters: list,
    hideCharacters: list,

    skipSSL: bool,
    followRedirect: bool,
    httpProxies: list,
    httpsProxies: list
):
    try:
        headers["User-Agent"] = userAgent[random.randint(
            0, len(userAgent) - 1)].rstrip()

        # Requests
        package = sendR(
            url= url,

            cookies= cookies,
            headers = headers,

            skipSSL= skipSSL,
            followRedirect= followRedirect,
            httpProxies= httpProxies,
            httpsProxies= httpsProxies
        )

        statusCode = package.status_code
        
        soup = BeautifulSoup(package.text, 'html.parser')
        words_len = len(extract_wordlist(soup))

        if (avaliableCharacters == None and hideCharacters == None and avaliableHTTPCodes == None and hideHTTPCodes == None):
            checkStatus.defaultProcess(
                status_Code=statusCode,
                words_len=words_len,
                url=url
            )

        # Check status in status code
        elif (avaliableCharacters == None and hideCharacters == None):
            checkStatus.analyzeStatusCode(
                hideHTTPCodes=hideHTTPCodes,
                avaliableHTTPCodes=avaliableHTTPCodes,
                statusCode=statusCode,
                words_len=words_len,
                url=url
            )

        # Check status in return words
        else:
            checkStatus.analyzeWords(
                avaliableCharacters=avaliableCharacters,
                hideCharacters=hideCharacters,
                words_len=words_len,
                status_code=statusCode,
                url=url
            )

        # Delay
        if (delayParam != None):
            delay(delayParam)

        # Close request
        package.close()

    # except KeyboardInterrupt:
    #     print("[-] Force exit...")
    #     exit(1)

    # except requests.exceptions.Timeout:
    #     tryExceptRequests(
    #         url=url,
    #         hideHTTPCodes=hideHTTPCodes,
    #         avaliableHTTPCodes=avaliableHTTPCodes,
    #         hideCharacters=hideCharacters,
    #         avaliableCharacters=avaliableCharacters,
    #         delayParam=delayParam,
    #         cookies=cookies,
    #         headers=headers,
    #         skipSSL=skipSSL,
    #         userAgent=userAgent,
    #         followRedirect=followRedirect,
    #         httpProxies=httpProxies,
    #         httpsProxies=httpsProxies
    #     )

    # except requests.exceptions.TooManyRedirects as e:
    #     print(f"[-] Too many redirects ===> {url} ===> {e}")
    #     exit("[-] Closing attack...")

    except requests.exceptions.ProxyError as e:
        tryExceptRequests(
            url=url,
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

    # except requests.exceptions.SSLError as e:
    #     print(
    #         f"[-] Error in certified SSL. Please active skipInsecureSSL =====> {e}")
    #     exit("[-] Closing attack...")

    # except requests.exceptions.InvalidHeader as e:
    #     print(f"[-] Error in header. Have invalids parameters ==> {e}")
    #     exit("[-] Closing attack...")

    # except requests.exceptions.ConnectionError as e:
    #     pass

    except requests.exceptions.RequestException as e:
        tryExceptRequests(
            url=url,
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
=======
import random
import requests
import Modules.Module_FilterValues.filter as checkStatus
import time
import re
from bs4 import BeautifulSoup
requests.packages.urllib3.disable_warnings()

def sendR(
    url: str,

    cookies: dict,
    headers: dict,

    skipSSL: bool,
    followRedirect: bool,
    httpProxies: list,
    httpsProxies: list
):
    if ( len( httpProxies ) > 0 ):
        package = requests.get(
            url=url,
            timeout=20,
            headers=headers,
            cookies=cookies,
            verify=skipSSL,
            allow_redirects=followRedirect,
            proxies={
                "http": httpProxies[random.randint(0, len(httpProxies) - 1)],
                "https": httpsProxies[random.randint(0, len(httpsProxies) - 1)]
            }
        )
        
        return package

    else:
        package = requests.get(
            url=url,
            timeout=20,
            headers=headers,
            cookies=cookies,
            verify=skipSSL,
            allow_redirects=followRedirect
        )
        
        return package


def delay(param: float):
    time.sleep(float(param))


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


def tryExceptRequests(
    url: str,
    delayParam: float,

    cookies: dict,
    headers: dict,
    userAgent: list,

    hideHTTPCodes: list,
    avaliableHTTPCodes: list,
    avaliableCharacters: list,
    hideCharacters: list,

    skipSSL: bool,
    followRedirect: bool,
    httpProxies: list,
    httpsProxies: list
):
    try:
        headers["User-Agent"] = userAgent[random.randint(
            0, len(userAgent) - 1)].rstrip()

        # Requests
        package = sendR(
            url= url,

            cookies= cookies,
            headers = headers,

            skipSSL= skipSSL,
            followRedirect= followRedirect,
            httpProxies= httpProxies,
            httpsProxies= httpsProxies
        )

        statusCode = package.status_code
        
        soup = BeautifulSoup(package.text, 'html.parser')
        words_len = len(extract_wordlist(soup))

        if (avaliableCharacters == None and hideCharacters == None and avaliableHTTPCodes == None and hideHTTPCodes == None):
            checkStatus.defaultProcess(
                status_Code=statusCode,
                words_len=words_len,
                url=url
            )

        # Check status in status code
        elif (avaliableCharacters == None and hideCharacters == None):
            checkStatus.analyzeStatusCode(
                hideHTTPCodes=hideHTTPCodes,
                avaliableHTTPCodes=avaliableHTTPCodes,
                statusCode=statusCode,
                words_len=words_len,
                url=url
            )

        # Check status in return words
        else:
            checkStatus.analyzeWords(
                avaliableCharacters=avaliableCharacters,
                hideCharacters=hideCharacters,
                words_len=words_len,
                status_code=statusCode,
                url=url
            )

        # Delay
        if (delayParam != None):
            delay(delayParam)

        # Close request
        package.close()

    # except KeyboardInterrupt:
    #     print("[-] Force exit...")
    #     exit(1)

    # except requests.exceptions.Timeout:
    #     tryExceptRequests(
    #         url=url,
    #         hideHTTPCodes=hideHTTPCodes,
    #         avaliableHTTPCodes=avaliableHTTPCodes,
    #         hideCharacters=hideCharacters,
    #         avaliableCharacters=avaliableCharacters,
    #         delayParam=delayParam,
    #         cookies=cookies,
    #         headers=headers,
    #         skipSSL=skipSSL,
    #         userAgent=userAgent,
    #         followRedirect=followRedirect,
    #         httpProxies=httpProxies,
    #         httpsProxies=httpsProxies
    #     )

    # except requests.exceptions.TooManyRedirects as e:
    #     print(f"[-] Too many redirects ===> {url} ===> {e}")
    #     exit("[-] Closing attack...")

    except requests.exceptions.ProxyError as e:
        tryExceptRequests(
            url=url,
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

    # except requests.exceptions.SSLError as e:
    #     print(
    #         f"[-] Error in certified SSL. Please active skipInsecureSSL =====> {e}")
    #     exit("[-] Closing attack...")

    # except requests.exceptions.InvalidHeader as e:
    #     print(f"[-] Error in header. Have invalids parameters ==> {e}")
    #     exit("[-] Closing attack...")

    # except requests.exceptions.ConnectionError as e:
    #     pass

    except requests.exceptions.RequestException as e:
        tryExceptRequests(
            url=url,
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
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
