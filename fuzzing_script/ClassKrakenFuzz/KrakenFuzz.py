<<<<<<< HEAD
import Modules.Module_Prints.Parameters.param as DP
import Utilities.DefaultsDiccionaries.search as WL
import Utilities.Requests.GET.sendRequests as SR
import Utilities.URL.check as CHECK
import Modules.Module_UserAgents.userAgents as UA
import Utilities.HeadersCookies.createParam as CP
import Utilities.Proxy.extract as PR
import Utilities.Proxy.http_https as PR_Filter

class krakenFuzzInitializer():
    def __init__(
        self,
        url: str, 
        wordlist: str,
        cookies: str,
        headers: str,
    
        enableProxy: bool,
        followRedirect: bool,
        skipInsecureSSL: bool,
        subDomain: bool,
        
        timeout: int,
        userAgent: str,
        outputResults: bool,
        threats: int,

        delay: int,
        
        hideHTTPCodes: str,
        avaliableHTTPCodes: str,
        avaliableCharacters: str,
        hideCharacters: str,
        ):
        
        # -----------------------------------------------------------------------------------------------------------------------------------------

        # PRIMARY DATA OF ATTACKER
        self.url = url                                                # URL to test
        self.payloadWordList = wordlist                               # WordList to use
        
        # SECONDARY DATA OF ATTACKER
        self.cookies = cookies                                        # Cookies to send with payload
        self.followRedirect = followRedirect                          # When response has 301 (Redirect) and you want to follow
        self.skipInsecureSSL = skipInsecureSSL                        # Skip Insecure SSL of page
        self.subDomain = subDomain                                    # Search subDomains
        self.enableProxy = enableProxy                                # Enable proxy
        self.proxiesList = {}                                         # Proxies List
        self.proxiesListHTTP = {}                                     # HTTP Proxies List
        self.proxiesListHTTPS = {}                                    # HTTPS Proxies List
        
        self.timeout =  timeout                                       # Define time to end test
        self.userAgent = userAgent                                    # Set User-Agent different of requests library
        self.outputResults = outputResults                            # Export results into a txt file
        self.threats   = threats                                      # Threats to implement
        self.hideHTTPCodes = hideHTTPCodes                            # HTTP codes hidden
        self.avaliableHTTPCodes = avaliableHTTPCodes                  # HTTP codes avaliables
        self.delay = delay                                            # Delay in requests 
        self.avaliableCharacters = avaliableCharacters                # Characters avaliables
        self.hideCharacters = hideCharacters                          # Characters hidden
        self.headers = headers                                        # Headers send in requests
        
        # -----------------------------------------------------------------------------------------------------------------------------------------
        
        if (self.enableProxy):
            self.proxies()
        self.checkURL()
        self.loadPayload()
        self.loadUserAgents()
        self.loadHeadersCookies()
        self.__run()

    # Load payload of module: Module_DefaultsDiccionaries
    def loadPayload(self):
        DP.describeParameters(self)
        self.payloadWordList = WL.readtxt(self.payloadWordList)
        
    def loadHeadersCookies(self):
        try:
            self.headers = CP.headers(self)
        except:
            pass
        
        try:
            self.cookies = CP.cookies(self)
        except:
            pass
        
    # Load userAgents of module: Module_UserAgents
    def loadUserAgents(self):
        self.userAgent = UA.userAgents()
    
    # Check URL format
    def checkURL(self):
        CHECK.url(self.url)

    # Load proxies
    def proxies(self):
        self.proxiesList = PR.proxyUtility()
        self.proxiesListHTTP = PR_Filter.http(self.proxiesList)
        self.proxiesListHTTPS = PR_Filter.https(self.proxiesList)
        DP.warningProxyEnable()
        
    # Run requests into server...
    def __run(self):
        SR.runFuzz(
            wordList= self.payloadWordList,
            url= self.url,
            cookies= self.cookies,
            headers= self.headers,
            
            skipSSL= self.skipInsecureSSL,
            followRedirect= self.followRedirect,
            subDomain= self.subDomain,
            httpProxies= self.proxiesListHTTP,
            httpsProxies= self.proxiesListHTTPS,
            
            userAgent= self.userAgent,
            threads= self.threats,
            delayParam= self.delay,
            
            hideHTTPCodes= self.hideHTTPCodes,
            avaliableHTTPCodes= self.avaliableHTTPCodes,
            hideCharacters= self.hideCharacters,
            avaliableCharacters= self.avaliableCharacters,
            )
=======
import Modules.Module_Prints.Parameters.param as DP
import Utilities.DefaultsDiccionaries.search as WL
import Utilities.Requests.GET.sendRequests as SR
import Utilities.URL.check as CHECK
import Modules.Module_UserAgents.userAgents as UA
import Utilities.HeadersCookies.createParam as CP
import Utilities.Proxy.extract as PR
import Utilities.Proxy.http_https as PR_Filter

class krakenFuzzInitializer():
    def __init__(
        self,
        url: str, 
        wordlist: str,
        cookies: str,
        headers: str,
    
        enableProxy: bool,
        followRedirect: bool,
        skipInsecureSSL: bool,
        subDomain: bool,
        
        timeout: int,
        userAgent: str,
        outputResults: bool,
        threats: int,

        delay: int,
        
        hideHTTPCodes: str,
        avaliableHTTPCodes: str,
        avaliableCharacters: str,
        hideCharacters: str,
        ):
        
        # -----------------------------------------------------------------------------------------------------------------------------------------

        # PRIMARY DATA OF ATTACKER
        self.url = url                                                # URL to test
        self.payloadWordList = wordlist                               # WordList to use
        
        # SECONDARY DATA OF ATTACKER
        self.cookies = cookies                                        # Cookies to send with payload
        self.followRedirect = followRedirect                          # When response has 301 (Redirect) and you want to follow
        self.skipInsecureSSL = skipInsecureSSL                        # Skip Insecure SSL of page
        self.subDomain = subDomain                                    # Search subDomains
        self.enableProxy = enableProxy                                # Enable proxy
        self.proxiesList = {}                                         # Proxies List
        self.proxiesListHTTP = {}                                     # HTTP Proxies List
        self.proxiesListHTTPS = {}                                    # HTTPS Proxies List
        
        self.timeout =  timeout                                       # Define time to end test
        self.userAgent = userAgent                                    # Set User-Agent different of requests library
        self.outputResults = outputResults                            # Export results into a txt file
        self.threats   = threats                                      # Threats to implement
        self.hideHTTPCodes = hideHTTPCodes                            # HTTP codes hidden
        self.avaliableHTTPCodes = avaliableHTTPCodes                  # HTTP codes avaliables
        self.delay = delay                                            # Delay in requests 
        self.avaliableCharacters = avaliableCharacters                # Characters avaliables
        self.hideCharacters = hideCharacters                          # Characters hidden
        self.headers = headers                                        # Headers send in requests
        
        # -----------------------------------------------------------------------------------------------------------------------------------------
        
        if (self.enableProxy):
            self.proxies()
        self.checkURL()
        self.loadPayload()
        self.loadUserAgents()
        self.loadHeadersCookies()
        self.__run()

    # Load payload of module: Module_DefaultsDiccionaries
    def loadPayload(self):
        DP.describeParameters(self)
        self.payloadWordList = WL.readtxt(self.payloadWordList)
        
    def loadHeadersCookies(self):
        try:
            self.headers = CP.headers(self)
        except:
            pass
        
        try:
            self.cookies = CP.cookies(self)
        except:
            pass
        
    # Load userAgents of module: Module_UserAgents
    def loadUserAgents(self):
        self.userAgent = UA.userAgents()
    
    # Check URL format
    def checkURL(self):
        CHECK.url(self.url)

    # Load proxies
    def proxies(self):
        self.proxiesList = PR.proxyUtility()
        self.proxiesListHTTP = PR_Filter.http(self.proxiesList)
        self.proxiesListHTTPS = PR_Filter.https(self.proxiesList)
        DP.warningProxyEnable()
        
    # Run requests into server...
    def __run(self):
        SR.runFuzz(
            wordList= self.payloadWordList,
            url= self.url,
            cookies= self.cookies,
            headers= self.headers,
            
            skipSSL= self.skipInsecureSSL,
            followRedirect= self.followRedirect,
            subDomain= self.subDomain,
            httpProxies= self.proxiesListHTTP,
            httpsProxies= self.proxiesListHTTPS,
            
            userAgent= self.userAgent,
            threads= self.threats,
            delayParam= self.delay,
            
            hideHTTPCodes= self.hideHTTPCodes,
            avaliableHTTPCodes= self.avaliableHTTPCodes,
            hideCharacters= self.hideCharacters,
            avaliableCharacters= self.avaliableCharacters,
            )
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
        