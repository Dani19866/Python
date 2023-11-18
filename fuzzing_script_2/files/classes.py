<<<<<<< HEAD
import requests
import random
import numpy as np
from threading import Thread
from bs4 import BeautifulSoup
from colorama import Fore, Style

from files.utils.prevents import prints_error
from files.utils.responses import calcule_lenght

class Fuzzing():
    def __init__(
        self, method: str, url: str, wordlist: list, threads: int, cookies: dict, headers: dict, data: dict, userAgents: list,
        followRedirect: bool, skipSSL: bool, randomProxies: list, proxy: dict, hideCode: list, avaliableCode: list, hideLenght: list,
        avaliableLenght: list, subdomain: bool, outputResults: bool, delay: bool, extensions: list
    ) -> None:
        # ---------Variables---------
        # Most important
        self.method = method

        # Obligatory values
        self.url = url
        self.wordlist = wordlist

        # Secundary values
        self.threads = threads
        self.cookies = cookies
        self.headers = headers
        self.data = data
        self.extensions = extensions

        # Tertiary values
        self.userAgents = userAgents
        self.followRedirect = followRedirect
        self.skipSSL = skipSSL
        self.randomProxies = randomProxies
        self.proxy = proxy

        # Responses
        self.hideCode = hideCode
        self.avaliableCode = avaliableCode
        self.hideLenght = hideLenght
        self.avaliableLenght = avaliableLenght

        # Other options
        self.subdomain = subdomain
        self.outputResults = outputResults
        self.delay = delay

        # IGNORE VARIABLES
        self.threadsModule = []
        self.cutList = None
        self.reservedStatus = {
            200: Fore.GREEN + str(200) + Style.RESET_ALL,
            301: Fore.YELLOW + str(301) + Style.RESET_ALL,
            302: Fore.YELLOW + str(301) + Style.RESET_ALL,
            401: Fore.MAGENTA + str(401) + Style.RESET_ALL,
            403: Fore.CYAN + str(403) + Style.RESET_ALL,
            404: Fore.RED + str(404) + Style.RESET_ALL
        }

        # ---------Fuzzing---------
        self.init()

    # ---------------------------------------------------
    def init(self):
        # Thread x WordList
        self.cutList = np.array_split(self.wordlist, self.threads)

        # Extension 
        if self.extensions != []:
            for payloadList in self.cutList:
                t = Thread(target=self.fuzzExtensions, args=(payloadList,))
                self.threadsModule.append(t)
                t.start()
        # Domain | Subdomain 
        else:
            # With random proxies
            if self.randomProxies != False:
                for payloadList in self.cutList:
                    t = Thread(target=self.fuzzRandomProxies, args=(payloadList,))
                    self.threadsModule.append(t)
                    t.start()
            # Without random proxies
            else:
                for payloadList in self.cutList:
                    t = Thread(target=self.fuzz, args=(payloadList,))
                    self.threadsModule.append(t)
                    t.start()
    # ---------------------------------------------------  
    def fuzz(self, payloadList: list):
        for payload in payloadList:
            target = None
            self.headers["User-Agent"] = self.userAgents[ random.randint( 0, len(self.userAgents) - 1) ].rstrip()
            
            if payload.startswith("/"):
                target = self.url.replace("/kFuzz", payload)
            else:
                target = self.url.replace("kFuzz", payload)
        
            # Start Fuzzing
            if self.method == "GET":
                try:
                    res = requests.get(
                    # URL
                    url=target,

                    # Cookies | Headers | Data
                    cookies=self.cookies,
                    headers=self.headers,
                    data=self.data,

                    # SSL | Redirect
                    verify=self.skipSSL,
                    allow_redirects=self.followRedirect,
                    
                    # ETC
                    timeout= 20,
                    proxies= self.proxy
                )

                    attacked = res.url
                    status = res.status_code
                    soup = BeautifulSoup(res.text, 'html.parser')
                    lenght = len( calcule_lenght(soup) )
                    
                    self.responses(status= status, lenght= lenght, url= attacked)

                except requests.exceptions.ProxyError:
                    prints_error("Manual proxy is invalid, please check your proxy")
                        
                except requests.exceptions.TooManyRedirects:
                    prints_error("Verify redirects. Its too many redirects...")
                
                except requests.exceptions.SSLError:
                    prints_error("Verify SSL certificacion. Please active --skipSSL")
                    
                except requests.exceptions.InvalidHeader:
                    prints_error("Please check header key/value. Error in headers")
                    
                except requests.exceptions.ConnectionError:
                    prints_error("Error in connection...")

                except requests.exceptions.RequestException as e:
                    prints_error(f"Error unrecognized: {e}")

            if self.method == "POST":
                try:
                    res = requests.post(
                    # URL
                    url=target,

                    # Cookies | Headers | Data
                    cookies=self.cookies,
                    headers=self.headers,
                    data=self.data,

                    # SSL | Redirect
                    verify=self.skipSSL,
                    allow_redirects=self.followRedirect,
                    
                    # ETC
                    timeout= 20,
                    proxies= self.proxy
                )
                    
                    attacked = res.url
                    status = res.status_code
                    soup = BeautifulSoup(res.text, 'html.parser')
                    lenght = len( calcule_lenght(soup) )
                    
                    self.responses(status= status, lenght= lenght, url= attacked)

                except requests.exceptions.ProxyError:
                    prints_error("Manual proxy is invalid, please check your proxy")

                except requests.exceptions.TooManyRedirects:
                    prints_error("Verify redirects. Its too many redirects...")
                
                except requests.exceptions.SSLError:
                    prints_error("Verify SSL certificacion. Please active --skipSSL")
                    
                except requests.exceptions.InvalidHeader:
                    prints_error("Please check header key/value. Error in headers")
                    
                except requests.exceptions.ConnectionError:
                    prints_error("Error in connection...")

                except requests.exceptions.RequestException as e:
                    prints_error(f"Error unrecognized: {e}")

    def fuzzRandomProxies(self, payloadList: list):
        for payload in payloadList:
            target = None
            num = random.randint( 0, len(self.randomProxies) ) - 1
            self.headers["User-Agent"] = self.userAgents[ random.randint( 0, len(self.userAgents) - 1) ].rstrip()
            
            if payload.startswith("/"):
                target = self.url.replace("/kFuzz", payload)
            else:
                target = self.url.replace("kFuzz", payload)
            
            # Start Fuzzing
            if self.method == "GET":
                try:
                    res = requests.get(
                    # URL
                    url=target,

                    # Cookies | Headers | Data
                    cookies=self.cookies,
                    headers=self.headers,
                    data=self.data,

                    # SSL | Redirect
                    verify=self.skipSSL,
                    allow_redirects=self.followRedirect,
                    
                    # ETC
                    timeout= 20,
                    proxies= {"https": self.randomProxies[num]}
                    )

                    attacked = res.url
                    status = res.status_code
                    soup = BeautifulSoup(res.text, 'html.parser')
                    lenght = len( calcule_lenght(soup) )
                    
                    self.responses(status= status, lenght= lenght, url= attacked)

                except requests.exceptions.ProxyError:
                    self.fuzzRandomProxies([payload])
                        
                except requests.exceptions.TooManyRedirects:
                    prints_error("Verify redirects. Its too many redirects...")
                
                except requests.exceptions.SSLError:
                    prints_error("Verify SSL certificacion. Please active --skipSSL")
                    
                except requests.exceptions.InvalidHeader:
                    prints_error("Please check header key/value. Error in headers")
                    
                except requests.exceptions.ConnectionError:
                    prints_error("Error in connection...")

                except requests.exceptions.RequestException as e:
                    prints_error(f"Error unrecognized: {e}")

            if self.method == "POST":
                try:
                    res = requests.post(
                    # URL
                    url=target,

                    # Cookies | Headers | Data
                    cookies=self.cookies,
                    headers=self.headers,
                    data=self.data,

                    # SSL | Redirect
                    verify=self.skipSSL,
                    allow_redirects=self.followRedirect,
                    
                    # ETC
                    timeout= 20,
                    proxies= self.randomProxies[num]
                    )
                    
                    attacked = res.url
                    status = res.status_code
                    soup = BeautifulSoup(res.text, 'html.parser')
                    lenght = len( calcule_lenght(soup) )
                    
                    self.responses(status= status, lenght= lenght, url= attacked)

                except requests.exceptions.ProxyError:
                    self.fuzzRandomProxies([payload])

                except requests.exceptions.TooManyRedirects:
                    prints_error("Verify redirects. Its too many redirects...")
                
                except requests.exceptions.SSLError:
                    prints_error("Verify SSL certificacion. Please active --skipSSL")
                    
                except requests.exceptions.InvalidHeader:
                    prints_error("Please check header key/value. Error in headers")
                    
                except requests.exceptions.ConnectionError:
                    prints_error("Error in connection...")

                except requests.exceptions.RequestException as e:
                    prints_error(f"Error unrecognized: {e}")

    def fuzzExtensions(self, payloadList: list):
        for payload in payloadList:
            self.headers["User-Agent"] = self.userAgents[ random.randint( 0, len(self.userAgents) - 1) ].rstrip()
            
            for ext in self.extensions:
                target = None

                if payload.startswith("/"):
                    target = self.url.replace("/kFuzz", payload+ext)
                else:
                    target = self.url.replace("kFuzz", payload+ext)
                
                # Start Fuzzing
                if self.method == "GET":
                    try:
                        res = requests.get(
                        # URL
                        url=target,

                        # Cookies | Headers | Data
                        cookies=self.cookies,
                        headers=self.headers,
                        data=self.data,

                        # SSL | Redirect
                        verify=self.skipSSL,
                        allow_redirects=self.followRedirect,
                        
                        # ETC
                        timeout= 20,
                        proxies= self.proxy
                        )

                        attacked = res.url
                        status = res.status_code
                        soup = BeautifulSoup(res.text, 'html.parser')
                        lenght = len( calcule_lenght(soup) )
                        
                        self.responses(status= status, lenght= lenght, url= attacked)

                    except requests.exceptions.TooManyRedirects:
                        prints_error("Verify redirects. Its too many redirects...")
                    
                    except requests.exceptions.SSLError:
                        prints_error("Verify SSL certificacion. Please active --skipSSL")
                        
                    except requests.exceptions.InvalidHeader:
                        prints_error("Please check header key/value. Error in headers")
                        
                    except requests.exceptions.ConnectionError:
                        prints_error("Error in connection...")

                    except requests.exceptions.RequestException as e:
                        prints_error(f"Error unrecognized: {e}")

                if self.method == "POST":
                    try:
                        res = requests.post(
                        # URL
                        url=target,

                        # Cookies | Headers | Data
                        cookies=self.cookies,
                        headers=self.headers,
                        data=self.data,

                        # SSL | Redirect
                        verify=self.skipSSL,
                        allow_redirects=self.followRedirect,
                        
                        # ETC
                        timeout= 20,
                        proxies= self.proxy
                        )

                        attacked = res.url
                        status = res.status_code
                        soup = BeautifulSoup(res.text, 'html.parser')
                        lenght = len( calcule_lenght(soup) )
                        
                        self.responses(status= status, lenght= lenght, url= attacked)

                    except requests.exceptions.TooManyRedirects:
                        prints_error("Verify redirects. Its too many redirects...")
                    
                    except requests.exceptions.SSLError:
                        prints_error("Verify SSL certificacion. Please active --skipSSL")
                        
                    except requests.exceptions.InvalidHeader:
                        prints_error("Please check header key/value. Error in headers")
                        
                    except requests.exceptions.ConnectionError:
                        prints_error("Error in connection...")

                    except requests.exceptions.RequestException as e:
                        prints_error(f"Error unrecognized: {e}")
    # ---------------------------------------------------
    def responses(self, status: int, lenght: int, url: str):
        # No filter
        if self.avaliableCode == None and self.hideCode == None and self.avaliableLenght == None and self.hideLenght == None:
            self.responses_extension(status, lenght, url)
        
        # Status filter
        elif self.hideCode != None or self.avaliableCode != None:
            # Filter hide code
            if self.hideCode != None:
                if str(status) in self.hideCode:
                    pass
                else:
                    self.responses_extension(status, lenght, url)
            # Filter avaliable code
            elif self.avaliableCode != None:
                if str(status) in self.avaliableCode:
                    self.responses_extension(status, lenght, url)
        
        # Lenght filter
        elif self.hideLenght != None or self.avaliableLenght != None:
            # Filter hide lenght
            if self.hideLenght != None:
                if str(lenght) in self.hideLenght:
                    pass
                else:
                    self.responses_extension(status, lenght, url)
            # Filter avaliable lenght
            elif self.avaliableLenght != None:
                if str(lenght) in self.avaliableLenght:
                    self.responses_extension(status, lenght, url)
                
    def responses_extension(self, status: int, lenght: int, url: str):
        point = 105
        minPoint = 90
        checkColor = True
        
        while True:
            # Lenght of URL
            urlLenght = len(url)
            
            # URL large in pont
            if urlLenght == point:
                # Check if in reserved status
                for reserved in self.reservedStatus:
                    # If in, print with her color
                    if status == reserved:
                        # Have lenght responses?
                        if lenght != 0:
                            print(url, self.reservedStatus[status], f"                  {lenght}")
                        else:
                            print(url, self.reservedStatus[status], f"                  {lenght}")
                        checkColor = False
                        return
                    
                # If not in, print without color
                if checkColor:
                    # Have lenght responses?
                    if lenght != 0:
                        print(url, status, f"                  {lenght}")
                    else:
                        print(url, status, f"                  {lenght}")
                    return
                    
            # Adjust large
            if urlLenght >= minPoint:
                # Plus spaces: Si el largo es mayor o igual que el mínimo y el largo es menor que el punto (Si es mayor, se sale de la regla)
                if urlLenght >= minPoint and urlLenght <point:
                    url = url + " "
                
                # Rest spaces
                if urlLenght > point:
                    url = url.replace(" ", "", 1)
            
            # Shortcut to adjust large
            else:
                url = url + "                "
=======
import requests
import random
import numpy as np
from threading import Thread
from bs4 import BeautifulSoup
from colorama import Fore, Style

from files.utils.prevents import prints_error
from files.utils.responses import calcule_lenght

class Fuzzing():
    def __init__(
        self, method: str, url: str, wordlist: list, threads: int, cookies: dict, headers: dict, data: dict, userAgents: list,
        followRedirect: bool, skipSSL: bool, randomProxies: list, proxy: dict, hideCode: list, avaliableCode: list, hideLenght: list,
        avaliableLenght: list, subdomain: bool, outputResults: bool, delay: bool, extensions: list
    ) -> None:
        # ---------Variables---------
        # Most important
        self.method = method

        # Obligatory values
        self.url = url
        self.wordlist = wordlist

        # Secundary values
        self.threads = threads
        self.cookies = cookies
        self.headers = headers
        self.data = data
        self.extensions = extensions

        # Tertiary values
        self.userAgents = userAgents
        self.followRedirect = followRedirect
        self.skipSSL = skipSSL
        self.randomProxies = randomProxies
        self.proxy = proxy

        # Responses
        self.hideCode = hideCode
        self.avaliableCode = avaliableCode
        self.hideLenght = hideLenght
        self.avaliableLenght = avaliableLenght

        # Other options
        self.subdomain = subdomain
        self.outputResults = outputResults
        self.delay = delay

        # IGNORE VARIABLES
        self.threadsModule = []
        self.cutList = None
        self.reservedStatus = {
            200: Fore.GREEN + str(200) + Style.RESET_ALL,
            301: Fore.YELLOW + str(301) + Style.RESET_ALL,
            302: Fore.YELLOW + str(301) + Style.RESET_ALL,
            401: Fore.MAGENTA + str(401) + Style.RESET_ALL,
            403: Fore.CYAN + str(403) + Style.RESET_ALL,
            404: Fore.RED + str(404) + Style.RESET_ALL
        }

        # ---------Fuzzing---------
        self.init()

    # ---------------------------------------------------
    def init(self):
        # Thread x WordList
        self.cutList = np.array_split(self.wordlist, self.threads)

        # Extension 
        if self.extensions != []:
            for payloadList in self.cutList:
                t = Thread(target=self.fuzzExtensions, args=(payloadList,))
                self.threadsModule.append(t)
                t.start()
        # Domain | Subdomain 
        else:
            # With random proxies
            if self.randomProxies != False:
                for payloadList in self.cutList:
                    t = Thread(target=self.fuzzRandomProxies, args=(payloadList,))
                    self.threadsModule.append(t)
                    t.start()
            # Without random proxies
            else:
                for payloadList in self.cutList:
                    t = Thread(target=self.fuzz, args=(payloadList,))
                    self.threadsModule.append(t)
                    t.start()
    # ---------------------------------------------------  
    def fuzz(self, payloadList: list):
        for payload in payloadList:
            target = None
            self.headers["User-Agent"] = self.userAgents[ random.randint( 0, len(self.userAgents) - 1) ].rstrip()
            
            if payload.startswith("/"):
                target = self.url.replace("/kFuzz", payload)
            else:
                target = self.url.replace("kFuzz", payload)
        
            # Start Fuzzing
            if self.method == "GET":
                try:
                    res = requests.get(
                    # URL
                    url=target,

                    # Cookies | Headers | Data
                    cookies=self.cookies,
                    headers=self.headers,
                    data=self.data,

                    # SSL | Redirect
                    verify=self.skipSSL,
                    allow_redirects=self.followRedirect,
                    
                    # ETC
                    timeout= 20,
                    proxies= self.proxy
                )

                    attacked = res.url
                    status = res.status_code
                    soup = BeautifulSoup(res.text, 'html.parser')
                    lenght = len( calcule_lenght(soup) )
                    
                    self.responses(status= status, lenght= lenght, url= attacked)

                except requests.exceptions.ProxyError:
                    prints_error("Manual proxy is invalid, please check your proxy")
                        
                except requests.exceptions.TooManyRedirects:
                    prints_error("Verify redirects. Its too many redirects...")
                
                except requests.exceptions.SSLError:
                    prints_error("Verify SSL certificacion. Please active --skipSSL")
                    
                except requests.exceptions.InvalidHeader:
                    prints_error("Please check header key/value. Error in headers")
                    
                except requests.exceptions.ConnectionError:
                    prints_error("Error in connection...")

                except requests.exceptions.RequestException as e:
                    prints_error(f"Error unrecognized: {e}")

            if self.method == "POST":
                try:
                    res = requests.post(
                    # URL
                    url=target,

                    # Cookies | Headers | Data
                    cookies=self.cookies,
                    headers=self.headers,
                    data=self.data,

                    # SSL | Redirect
                    verify=self.skipSSL,
                    allow_redirects=self.followRedirect,
                    
                    # ETC
                    timeout= 20,
                    proxies= self.proxy
                )
                    
                    attacked = res.url
                    status = res.status_code
                    soup = BeautifulSoup(res.text, 'html.parser')
                    lenght = len( calcule_lenght(soup) )
                    
                    self.responses(status= status, lenght= lenght, url= attacked)

                except requests.exceptions.ProxyError:
                    prints_error("Manual proxy is invalid, please check your proxy")

                except requests.exceptions.TooManyRedirects:
                    prints_error("Verify redirects. Its too many redirects...")
                
                except requests.exceptions.SSLError:
                    prints_error("Verify SSL certificacion. Please active --skipSSL")
                    
                except requests.exceptions.InvalidHeader:
                    prints_error("Please check header key/value. Error in headers")
                    
                except requests.exceptions.ConnectionError:
                    prints_error("Error in connection...")

                except requests.exceptions.RequestException as e:
                    prints_error(f"Error unrecognized: {e}")

    def fuzzRandomProxies(self, payloadList: list):
        for payload in payloadList:
            target = None
            num = random.randint( 0, len(self.randomProxies) ) - 1
            self.headers["User-Agent"] = self.userAgents[ random.randint( 0, len(self.userAgents) - 1) ].rstrip()
            
            if payload.startswith("/"):
                target = self.url.replace("/kFuzz", payload)
            else:
                target = self.url.replace("kFuzz", payload)
            
            # Start Fuzzing
            if self.method == "GET":
                try:
                    res = requests.get(
                    # URL
                    url=target,

                    # Cookies | Headers | Data
                    cookies=self.cookies,
                    headers=self.headers,
                    data=self.data,

                    # SSL | Redirect
                    verify=self.skipSSL,
                    allow_redirects=self.followRedirect,
                    
                    # ETC
                    timeout= 20,
                    proxies= {"https": self.randomProxies[num]}
                    )

                    attacked = res.url
                    status = res.status_code
                    soup = BeautifulSoup(res.text, 'html.parser')
                    lenght = len( calcule_lenght(soup) )
                    
                    self.responses(status= status, lenght= lenght, url= attacked)

                except requests.exceptions.ProxyError:
                    self.fuzzRandomProxies([payload])
                        
                except requests.exceptions.TooManyRedirects:
                    prints_error("Verify redirects. Its too many redirects...")
                
                except requests.exceptions.SSLError:
                    prints_error("Verify SSL certificacion. Please active --skipSSL")
                    
                except requests.exceptions.InvalidHeader:
                    prints_error("Please check header key/value. Error in headers")
                    
                except requests.exceptions.ConnectionError:
                    prints_error("Error in connection...")

                except requests.exceptions.RequestException as e:
                    prints_error(f"Error unrecognized: {e}")

            if self.method == "POST":
                try:
                    res = requests.post(
                    # URL
                    url=target,

                    # Cookies | Headers | Data
                    cookies=self.cookies,
                    headers=self.headers,
                    data=self.data,

                    # SSL | Redirect
                    verify=self.skipSSL,
                    allow_redirects=self.followRedirect,
                    
                    # ETC
                    timeout= 20,
                    proxies= self.randomProxies[num]
                    )
                    
                    attacked = res.url
                    status = res.status_code
                    soup = BeautifulSoup(res.text, 'html.parser')
                    lenght = len( calcule_lenght(soup) )
                    
                    self.responses(status= status, lenght= lenght, url= attacked)

                except requests.exceptions.ProxyError:
                    self.fuzzRandomProxies([payload])

                except requests.exceptions.TooManyRedirects:
                    prints_error("Verify redirects. Its too many redirects...")
                
                except requests.exceptions.SSLError:
                    prints_error("Verify SSL certificacion. Please active --skipSSL")
                    
                except requests.exceptions.InvalidHeader:
                    prints_error("Please check header key/value. Error in headers")
                    
                except requests.exceptions.ConnectionError:
                    prints_error("Error in connection...")

                except requests.exceptions.RequestException as e:
                    prints_error(f"Error unrecognized: {e}")

    def fuzzExtensions(self, payloadList: list):
        for payload in payloadList:
            self.headers["User-Agent"] = self.userAgents[ random.randint( 0, len(self.userAgents) - 1) ].rstrip()
            
            for ext in self.extensions:
                target = None

                if payload.startswith("/"):
                    target = self.url.replace("/kFuzz", payload+ext)
                else:
                    target = self.url.replace("kFuzz", payload+ext)
                
                # Start Fuzzing
                if self.method == "GET":
                    try:
                        res = requests.get(
                        # URL
                        url=target,

                        # Cookies | Headers | Data
                        cookies=self.cookies,
                        headers=self.headers,
                        data=self.data,

                        # SSL | Redirect
                        verify=self.skipSSL,
                        allow_redirects=self.followRedirect,
                        
                        # ETC
                        timeout= 20,
                        proxies= self.proxy
                        )

                        attacked = res.url
                        status = res.status_code
                        soup = BeautifulSoup(res.text, 'html.parser')
                        lenght = len( calcule_lenght(soup) )
                        
                        self.responses(status= status, lenght= lenght, url= attacked)

                    except requests.exceptions.TooManyRedirects:
                        prints_error("Verify redirects. Its too many redirects...")
                    
                    except requests.exceptions.SSLError:
                        prints_error("Verify SSL certificacion. Please active --skipSSL")
                        
                    except requests.exceptions.InvalidHeader:
                        prints_error("Please check header key/value. Error in headers")
                        
                    except requests.exceptions.ConnectionError:
                        prints_error("Error in connection...")

                    except requests.exceptions.RequestException as e:
                        prints_error(f"Error unrecognized: {e}")

                if self.method == "POST":
                    try:
                        res = requests.post(
                        # URL
                        url=target,

                        # Cookies | Headers | Data
                        cookies=self.cookies,
                        headers=self.headers,
                        data=self.data,

                        # SSL | Redirect
                        verify=self.skipSSL,
                        allow_redirects=self.followRedirect,
                        
                        # ETC
                        timeout= 20,
                        proxies= self.proxy
                        )

                        attacked = res.url
                        status = res.status_code
                        soup = BeautifulSoup(res.text, 'html.parser')
                        lenght = len( calcule_lenght(soup) )
                        
                        self.responses(status= status, lenght= lenght, url= attacked)

                    except requests.exceptions.TooManyRedirects:
                        prints_error("Verify redirects. Its too many redirects...")
                    
                    except requests.exceptions.SSLError:
                        prints_error("Verify SSL certificacion. Please active --skipSSL")
                        
                    except requests.exceptions.InvalidHeader:
                        prints_error("Please check header key/value. Error in headers")
                        
                    except requests.exceptions.ConnectionError:
                        prints_error("Error in connection...")

                    except requests.exceptions.RequestException as e:
                        prints_error(f"Error unrecognized: {e}")
    # ---------------------------------------------------
    def responses(self, status: int, lenght: int, url: str):
        # No filter
        if self.avaliableCode == None and self.hideCode == None and self.avaliableLenght == None and self.hideLenght == None:
            self.responses_extension(status, lenght, url)
        
        # Status filter
        elif self.hideCode != None or self.avaliableCode != None:
            # Filter hide code
            if self.hideCode != None:
                if str(status) in self.hideCode:
                    pass
                else:
                    self.responses_extension(status, lenght, url)
            # Filter avaliable code
            elif self.avaliableCode != None:
                if str(status) in self.avaliableCode:
                    self.responses_extension(status, lenght, url)
        
        # Lenght filter
        elif self.hideLenght != None or self.avaliableLenght != None:
            # Filter hide lenght
            if self.hideLenght != None:
                if str(lenght) in self.hideLenght:
                    pass
                else:
                    self.responses_extension(status, lenght, url)
            # Filter avaliable lenght
            elif self.avaliableLenght != None:
                if str(lenght) in self.avaliableLenght:
                    self.responses_extension(status, lenght, url)
                
    def responses_extension(self, status: int, lenght: int, url: str):
        point = 105
        minPoint = 90
        checkColor = True
        
        while True:
            # Lenght of URL
            urlLenght = len(url)
            
            # URL large in pont
            if urlLenght == point:
                # Check if in reserved status
                for reserved in self.reservedStatus:
                    # If in, print with her color
                    if status == reserved:
                        # Have lenght responses?
                        if lenght != 0:
                            print(url, self.reservedStatus[status], f"                  {lenght}")
                        else:
                            print(url, self.reservedStatus[status], f"                  {lenght}")
                        checkColor = False
                        return
                    
                # If not in, print without color
                if checkColor:
                    # Have lenght responses?
                    if lenght != 0:
                        print(url, status, f"                  {lenght}")
                    else:
                        print(url, status, f"                  {lenght}")
                    return
                    
            # Adjust large
            if urlLenght >= minPoint:
                # Plus spaces: Si el largo es mayor o igual que el mínimo y el largo es menor que el punto (Si es mayor, se sale de la regla)
                if urlLenght >= minPoint and urlLenght <point:
                    url = url + " "
                
                # Rest spaces
                if urlLenght > point:
                    url = url.replace(" ", "", 1)
            
            # Shortcut to adjust large
            else:
                url = url + "                "
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
    # ---------------------------------------------------