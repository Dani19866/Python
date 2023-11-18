<<<<<<< HEAD
from files.cli import load_parser
from files.utils.prevents import prints_error,prints_verified, print_exit
from files.utils.prints import presentation, table
from files.utils.proxy import proxyUtility, onlyHTTPS
from files.classes import Fuzzing

# Global variables
url = None
wordlist = None
method = None
cookies = None
headers = None
threads = None
extensions = None
data = None
random_useragent = None
followRedirect = None
skipSSL = None
random_proxies = None
proxy = None
hidecode = None
hidelenght = None
avaliablecode = None
avaliablelenght = None

# Variables to modify in Class
subdomain = None
outputResults = None
delay = None

# Utils functions
def load_values():
    global url
    global wordlist
    global method
    global cookies
    global headers
    global threads
    global extensions
    global data
    global random_useragent
    global followRedirect
    global skipSSL
    global random_proxies
    global proxy
    global hidecode
    global hidelenght
    global avaliablecode
    global avaliablelenght
    global subdomain
    global outputResults
    global delay

    # ----------------------------------------------------------------------------------------
    # Obligatory values
    url = load_parser().url
    wordlist = load_parser().wordlist
    method = load_parser().method
    
    # ----------------------------------------------------------------------------------------
    # Secundary values
    cookies = load_parser().cookies
    headers = load_parser().headers
    threads = load_parser().threads
    extensions = load_parser().extensions
    data = load_parser().data
    
    # ----------------------------------------------------------------------------------------
    # Tertiary values
    random_useragent = load_parser().random_useragent
    followRedirect = load_parser().followRedirect
    skipSSL = load_parser().skipSSL
    random_proxies = load_parser().random_proxies
    proxy = load_parser().proxy
    
    # ----------------------------------------------------------------------------------------
    # Responses
    hidecode = load_parser().hidecode
    hidelenght = load_parser().hidelenght
    avaliablecode = load_parser().avaliablecode
    avaliablelenght = load_parser().avaliablelenght
    
    # ----------------------------------------------------------------------------------------
    # Other options
    subdomain = load_parser().subdomain
    outputResults = load_parser().outputResults
    delay = load_parser().delay

def load_prevents():
    # Check HTTP/HTTPs
    if "http://" in url.lower() or "https://" in url.lower():
        pass
    else:
        prints_error("URL param no has HTTP:// or HTTPS://")
        
    # Check kFuzz in subdomain
    if subdomain:
        verify = url.find("https://kFuzz")
        if verify == -1:
            prints_error("You dont have kFuzz in domain... https://kFuzz.example.com")
        
    # Check kFuzz
    verify = url.find("kFuzz")
    if verify == -1:
        prints_error("Not found kFuzz keyword")
        
    # Check method
    if "GET" in method or "POST" in method:
        pass
    else:
        prints_error("The method is invalid!")

    prints_verified("URL and Method checked!")

def load_cookies_headers_data():
    global headers, cookies, data
    
    # ----------------------------------------------------------------------------------------
    # Header
    temp = headers.split("&")
    count = 0
    tempIndex = None
    tempData = None
    definitive = {}
    
    for x in temp:
            x = x.split("=")

            for y in x:
                if count == 0:
                    tempIndex = y
                    count = 1

                elif count == 1:
                    tempData = y
                    count = 2

            # Add into a dictionary
            if count == 2:
                definitive[tempIndex] = tempData
                count = 0
    
    # ----------------------------------------------------------------------------------------
    headers = definitive
    # ----------------------------------------------------------------------------------------
    
    # ----------------------------------------------------------------------------------------
    # Cookie
    temp = cookies.split("&")
    count = 0
    tempIndex = None
    tempData = None
    definitive = {}
    
    for x in temp:
            x = x.split("=")

            for y in x:
                if count == 0:
                    tempIndex = y
                    count = 1

                elif count == 1:
                    tempData = y
                    count = 2

            # Add into a dictionary
            if count == 2:
                definitive[tempIndex] = tempData
                count = 0
                
    # ----------------------------------------------------------------------------------------
    cookies = definitive
    # ----------------------------------------------------------------------------------------
    
    # ----------------------------------------------------------------------------------------
    # Data
    temp = data.split("&")
    count = 0
    tempIndex = None
    tempData = None
    definitive = {}
    
    for x in temp:
            x = x.split("=")

            for y in x:
                if count == 0:
                    tempIndex = y
                    count = 1

                elif count == 1:
                    tempData = y
                    count = 2

            # Add into a dictionary
            if count == 2:
                definitive[tempIndex] = tempData
                count = 0
                
    # ----------------------------------------------------------------------------------------
    data = definitive
    
    prints_verified("Headers, cookies and data checked and structured!")

def load_userAgents_wordlist(path: str):
    global random_useragent, wordlist
    verify = False
    
    if random_useragent == False:
        pass
    else:
        verify = True
    
    # User-Agents
    fileRead = open("files/User-Agent/file.txt", "r").read()
    random_useragent = fileRead.split("\n")
    
    # WordList
    fileRead = open(path, "r", encoding="utf8").read().rstrip()
    wordlist = fileRead.split("\n")
    
    if verify == False:
        prints_verified("Wordlist ready!")
    else:
        prints_verified("User-Agents and wordlist ready!")

def load_hide_avaliable_responses():
    global hidecode, avaliablecode, hidelenght, avaliablelenght
    
    try:
        if (hidecode != None):
            hidecode = hidecode.split(",")
            prints_verified("Responses filter ready!")
            
        elif (avaliablecode != None):
            avaliablecode = avaliablecode.split(",")
            prints_verified("Responses filter ready!")
    except:
        pass
    
    try:
        if (hidelenght != None):
            hidelenght = hidelenght.split(",")
            prints_verified("Responses filter ready!")
            
        elif (avaliablelenght != None):
            avaliablelenght = avaliablelenght.split(",")
            prints_verified("Responses filter ready!")
    except:
        pass

def load_proxies():
    global proxy, random_proxies
    
    # Prevent error
    if random_proxies == True and proxy != {}:
        prints_error("Random proxies and manual proxy has active! Please select one no both")
    
    # Work with random proxies
    if random_proxies == True:
        list_of_proxies = proxyUtility()
        random_proxies = onlyHTTPS(list_of_proxies)
        
        prints_verified("Random HTTPS proxies ready!")
        
    # Word with manual proxy
    if proxy != {}:
        temp = proxy.split(":")
        proxy = {}
        # Prevent error
        if len(temp) > 3:
            prints_error("Check manual proxy, the entry of data is *method*:*ip*:*port*")
        
        method_proxy = temp[0]
        ip_proxy = f"{temp[1]}:{temp[2]}"
        proxy[method_proxy] = ip_proxy
        
        prints_verified("Proxy ready!")

def load_extensions():
    global extensions
    
    if "/" in extensions or "\\" in extensions:
        extensions = open(extensions, "r").read().split("\n")
        prints_verified("Extensions ready!")
        
    elif extensions != "":
        extensions = extensions.split(",")
        prints_verified("Extensions ready!")
    
    else:
        extensions = []
        
# Principal functions
def load_presentation():
    presentation()

def load_classes():
    table()
    
    if method.lower() == "get":
        Fuzzing(
            # The most important
            method= "GET",
            
            extensions= extensions,
            url= url,
            wordlist= wordlist,
            threads= threads,
            cookies= cookies,
            headers= headers,
            data= data,
            userAgents= random_useragent,
            followRedirect= followRedirect,
            skipSSL= skipSSL,
            randomProxies= random_proxies,
            proxy= proxy,
            hideCode= hidecode,
            avaliableCode= avaliablecode,
            hideLenght= hidelenght,
            avaliableLenght= avaliablelenght,
            subdomain= subdomain,
            outputResults= outputResults,
            delay= delay
        )
    
    if method.lower() == "post":
        Fuzzing(
            # The most important
            method= "POST",
            
            extensions= extensions,
            url= url,
            wordlist= wordlist,
            threads= threads,
            cookies= cookies,
            headers= headers,
            data= data,
            userAgents= random_useragent,
            followRedirect= followRedirect,
            skipSSL= skipSSL,
            randomProxies= random_proxies,
            proxy= proxy,
            hideCode= hidecode,
            avaliableCode= avaliablecode,
            hideLenght= hidelenght,
            avaliableLenght= avaliablelenght,
            subdomain= subdomain,
            outputResults= outputResults,
            delay= delay
        )

if __name__ == "__main__":
    try:
        # If its ok all data, load presentation
        load_presentation()
        
        # Extract values of parser
        load_values()
        # Prevents error of software
        load_prevents()
        # Load and structure cookies, headers and GET/POST data
        load_cookies_headers_data()
        # Load and structure randomUseragents and wordlist
        load_userAgents_wordlist(wordlist)
        # Load and structure hide and avaliable responses
        load_hide_avaliable_responses()
        # Load and structure proxies
        load_proxies()
        # Load extensions
        load_extensions()
        
        # Load classes
        load_classes()
        
    except KeyboardInterrupt:
=======
from files.cli import load_parser
from files.utils.prevents import prints_error,prints_verified, print_exit
from files.utils.prints import presentation, table
from files.utils.proxy import proxyUtility, onlyHTTPS
from files.classes import Fuzzing

# Global variables
url = None
wordlist = None
method = None
cookies = None
headers = None
threads = None
extensions = None
data = None
random_useragent = None
followRedirect = None
skipSSL = None
random_proxies = None
proxy = None
hidecode = None
hidelenght = None
avaliablecode = None
avaliablelenght = None

# Variables to modify in Class
subdomain = None
outputResults = None
delay = None

# Utils functions
def load_values():
    global url
    global wordlist
    global method
    global cookies
    global headers
    global threads
    global extensions
    global data
    global random_useragent
    global followRedirect
    global skipSSL
    global random_proxies
    global proxy
    global hidecode
    global hidelenght
    global avaliablecode
    global avaliablelenght
    global subdomain
    global outputResults
    global delay

    # ----------------------------------------------------------------------------------------
    # Obligatory values
    url = load_parser().url
    wordlist = load_parser().wordlist
    method = load_parser().method
    
    # ----------------------------------------------------------------------------------------
    # Secundary values
    cookies = load_parser().cookies
    headers = load_parser().headers
    threads = load_parser().threads
    extensions = load_parser().extensions
    data = load_parser().data
    
    # ----------------------------------------------------------------------------------------
    # Tertiary values
    random_useragent = load_parser().random_useragent
    followRedirect = load_parser().followRedirect
    skipSSL = load_parser().skipSSL
    random_proxies = load_parser().random_proxies
    proxy = load_parser().proxy
    
    # ----------------------------------------------------------------------------------------
    # Responses
    hidecode = load_parser().hidecode
    hidelenght = load_parser().hidelenght
    avaliablecode = load_parser().avaliablecode
    avaliablelenght = load_parser().avaliablelenght
    
    # ----------------------------------------------------------------------------------------
    # Other options
    subdomain = load_parser().subdomain
    outputResults = load_parser().outputResults
    delay = load_parser().delay

def load_prevents():
    # Check HTTP/HTTPs
    if "http://" in url.lower() or "https://" in url.lower():
        pass
    else:
        prints_error("URL param no has HTTP:// or HTTPS://")
        
    # Check kFuzz in subdomain
    if subdomain:
        verify = url.find("https://kFuzz")
        if verify == -1:
            prints_error("You dont have kFuzz in domain... https://kFuzz.example.com")
        
    # Check kFuzz
    verify = url.find("kFuzz")
    if verify == -1:
        prints_error("Not found kFuzz keyword")
        
    # Check method
    if "GET" in method or "POST" in method:
        pass
    else:
        prints_error("The method is invalid!")

    prints_verified("URL and Method checked!")

def load_cookies_headers_data():
    global headers, cookies, data
    
    # ----------------------------------------------------------------------------------------
    # Header
    temp = headers.split("&")
    count = 0
    tempIndex = None
    tempData = None
    definitive = {}
    
    for x in temp:
            x = x.split("=")

            for y in x:
                if count == 0:
                    tempIndex = y
                    count = 1

                elif count == 1:
                    tempData = y
                    count = 2

            # Add into a dictionary
            if count == 2:
                definitive[tempIndex] = tempData
                count = 0
    
    # ----------------------------------------------------------------------------------------
    headers = definitive
    # ----------------------------------------------------------------------------------------
    
    # ----------------------------------------------------------------------------------------
    # Cookie
    temp = cookies.split("&")
    count = 0
    tempIndex = None
    tempData = None
    definitive = {}
    
    for x in temp:
            x = x.split("=")

            for y in x:
                if count == 0:
                    tempIndex = y
                    count = 1

                elif count == 1:
                    tempData = y
                    count = 2

            # Add into a dictionary
            if count == 2:
                definitive[tempIndex] = tempData
                count = 0
                
    # ----------------------------------------------------------------------------------------
    cookies = definitive
    # ----------------------------------------------------------------------------------------
    
    # ----------------------------------------------------------------------------------------
    # Data
    temp = data.split("&")
    count = 0
    tempIndex = None
    tempData = None
    definitive = {}
    
    for x in temp:
            x = x.split("=")

            for y in x:
                if count == 0:
                    tempIndex = y
                    count = 1

                elif count == 1:
                    tempData = y
                    count = 2

            # Add into a dictionary
            if count == 2:
                definitive[tempIndex] = tempData
                count = 0
                
    # ----------------------------------------------------------------------------------------
    data = definitive
    
    prints_verified("Headers, cookies and data checked and structured!")

def load_userAgents_wordlist(path: str):
    global random_useragent, wordlist
    verify = False
    
    if random_useragent == False:
        pass
    else:
        verify = True
    
    # User-Agents
    fileRead = open("files/User-Agent/file.txt", "r").read()
    random_useragent = fileRead.split("\n")
    
    # WordList
    fileRead = open(path, "r", encoding="utf8").read().rstrip()
    wordlist = fileRead.split("\n")
    
    if verify == False:
        prints_verified("Wordlist ready!")
    else:
        prints_verified("User-Agents and wordlist ready!")

def load_hide_avaliable_responses():
    global hidecode, avaliablecode, hidelenght, avaliablelenght
    
    try:
        if (hidecode != None):
            hidecode = hidecode.split(",")
            prints_verified("Responses filter ready!")
            
        elif (avaliablecode != None):
            avaliablecode = avaliablecode.split(",")
            prints_verified("Responses filter ready!")
    except:
        pass
    
    try:
        if (hidelenght != None):
            hidelenght = hidelenght.split(",")
            prints_verified("Responses filter ready!")
            
        elif (avaliablelenght != None):
            avaliablelenght = avaliablelenght.split(",")
            prints_verified("Responses filter ready!")
    except:
        pass

def load_proxies():
    global proxy, random_proxies
    
    # Prevent error
    if random_proxies == True and proxy != {}:
        prints_error("Random proxies and manual proxy has active! Please select one no both")
    
    # Work with random proxies
    if random_proxies == True:
        list_of_proxies = proxyUtility()
        random_proxies = onlyHTTPS(list_of_proxies)
        
        prints_verified("Random HTTPS proxies ready!")
        
    # Word with manual proxy
    if proxy != {}:
        temp = proxy.split(":")
        proxy = {}
        # Prevent error
        if len(temp) > 3:
            prints_error("Check manual proxy, the entry of data is *method*:*ip*:*port*")
        
        method_proxy = temp[0]
        ip_proxy = f"{temp[1]}:{temp[2]}"
        proxy[method_proxy] = ip_proxy
        
        prints_verified("Proxy ready!")

def load_extensions():
    global extensions
    
    if "/" in extensions or "\\" in extensions:
        extensions = open(extensions, "r").read().split("\n")
        prints_verified("Extensions ready!")
        
    elif extensions != "":
        extensions = extensions.split(",")
        prints_verified("Extensions ready!")
    
    else:
        extensions = []
        
# Principal functions
def load_presentation():
    presentation()

def load_classes():
    table()
    
    if method.lower() == "get":
        Fuzzing(
            # The most important
            method= "GET",
            
            extensions= extensions,
            url= url,
            wordlist= wordlist,
            threads= threads,
            cookies= cookies,
            headers= headers,
            data= data,
            userAgents= random_useragent,
            followRedirect= followRedirect,
            skipSSL= skipSSL,
            randomProxies= random_proxies,
            proxy= proxy,
            hideCode= hidecode,
            avaliableCode= avaliablecode,
            hideLenght= hidelenght,
            avaliableLenght= avaliablelenght,
            subdomain= subdomain,
            outputResults= outputResults,
            delay= delay
        )
    
    if method.lower() == "post":
        Fuzzing(
            # The most important
            method= "POST",
            
            extensions= extensions,
            url= url,
            wordlist= wordlist,
            threads= threads,
            cookies= cookies,
            headers= headers,
            data= data,
            userAgents= random_useragent,
            followRedirect= followRedirect,
            skipSSL= skipSSL,
            randomProxies= random_proxies,
            proxy= proxy,
            hideCode= hidecode,
            avaliableCode= avaliablecode,
            hideLenght= hidelenght,
            avaliableLenght= avaliablelenght,
            subdomain= subdomain,
            outputResults= outputResults,
            delay= delay
        )

if __name__ == "__main__":
    try:
        # If its ok all data, load presentation
        load_presentation()
        
        # Extract values of parser
        load_values()
        # Prevents error of software
        load_prevents()
        # Load and structure cookies, headers and GET/POST data
        load_cookies_headers_data()
        # Load and structure randomUseragents and wordlist
        load_userAgents_wordlist(wordlist)
        # Load and structure hide and avaliable responses
        load_hide_avaliable_responses()
        # Load and structure proxies
        load_proxies()
        # Load extensions
        load_extensions()
        
        # Load classes
        load_classes()
        
    except KeyboardInterrupt:
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
        print_exit("code 1")