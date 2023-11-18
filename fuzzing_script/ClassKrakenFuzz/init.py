<<<<<<< HEAD
import ClassKrakenFuzz.KrakenFuzz as Kraken
import CLI.CLIKrakenFuzz as CLI
import Utilities.DefaultsDiccionaries.search as WordLists

def runKraken(args):
    # PRIMARY DATA
    url = args.url
    wordlist = args.wordlist

    # SECUNDARY DATA // LARGUE DATA // Type: String
    cookies = args.cookies if args.cookies is not None else {}
    headers = args.headers if args.headers is not None else {}
    
    # SECUNDARY DATA // Type: String
    userAgent = args.userAgent if args.userAgent is not None else "Module_UserAgents\\user-agents.txt"
    hideHTTPCodes = args.hideHTTPCodes if args.hideHTTPCodes is not None else None
    avaliableHTTPCodes = args.avaliableHTTPCodes if args.avaliableHTTPCodes is not None else None
    avaliableCharacters = args.avaliableCharacters if args.avaliableCharacters is not None else None
    hideCharacters = args.hideCharacters if args.hideCharacters is not None else None

    # SECUNDARY DATA // Type: Bool
    followRedirect = args.followRedirect if args.followRedirect is not None else False
    skipInsecureSSL = args.skipInsecureSSL if args.skipInsecureSSL is not None else True
    outputResults = args.outputResults if args.outputResults is not None else False
    enableProxy = args.enableProxy if args.enableProxy is not None else False
    subDomain = args.subDomain if args.subDomain is not None else False

    # SECUNDARY DATA // Type: Int
    # 05 minutes for default
    timeout = args.timeOut if args.timeOut is not None else 5
    # 20 threats for default
    threats = args.threats if args.threats is not None else 20
    # None for default
    delay = args.delay if args.delay is not None else None
    
    wordlist = WordLists.AnalyzerParam(wordlist)

    Kraken.krakenFuzzInitializer(
        url= url,
        wordlist= wordlist,
        cookies= cookies,
        headers= headers,
        
        followRedirect= followRedirect,
        skipInsecureSSL= skipInsecureSSL,
        enableProxy= enableProxy,
        subDomain=subDomain,
        
        timeout= timeout,
        userAgent= userAgent,
        outputResults= outputResults,
        threats= threats,
        delay= delay,
        
        hideHTTPCodes= hideHTTPCodes,
        avaliableHTTPCodes= avaliableHTTPCodes,
        hideCharacters= hideCharacters,
        avaliableCharacters= avaliableCharacters,
=======
import ClassKrakenFuzz.KrakenFuzz as Kraken
import CLI.CLIKrakenFuzz as CLI
import Utilities.DefaultsDiccionaries.search as WordLists

def runKraken(args):
    # PRIMARY DATA
    url = args.url
    wordlist = args.wordlist

    # SECUNDARY DATA // LARGUE DATA // Type: String
    cookies = args.cookies if args.cookies is not None else {}
    headers = args.headers if args.headers is not None else {}
    
    # SECUNDARY DATA // Type: String
    userAgent = args.userAgent if args.userAgent is not None else "Module_UserAgents\\user-agents.txt"
    hideHTTPCodes = args.hideHTTPCodes if args.hideHTTPCodes is not None else None
    avaliableHTTPCodes = args.avaliableHTTPCodes if args.avaliableHTTPCodes is not None else None
    avaliableCharacters = args.avaliableCharacters if args.avaliableCharacters is not None else None
    hideCharacters = args.hideCharacters if args.hideCharacters is not None else None

    # SECUNDARY DATA // Type: Bool
    followRedirect = args.followRedirect if args.followRedirect is not None else False
    skipInsecureSSL = args.skipInsecureSSL if args.skipInsecureSSL is not None else True
    outputResults = args.outputResults if args.outputResults is not None else False
    enableProxy = args.enableProxy if args.enableProxy is not None else False
    subDomain = args.subDomain if args.subDomain is not None else False

    # SECUNDARY DATA // Type: Int
    # 05 minutes for default
    timeout = args.timeOut if args.timeOut is not None else 5
    # 20 threats for default
    threats = args.threats if args.threats is not None else 20
    # None for default
    delay = args.delay if args.delay is not None else None
    
    wordlist = WordLists.AnalyzerParam(wordlist)

    Kraken.krakenFuzzInitializer(
        url= url,
        wordlist= wordlist,
        cookies= cookies,
        headers= headers,
        
        followRedirect= followRedirect,
        skipInsecureSSL= skipInsecureSSL,
        enableProxy= enableProxy,
        subDomain=subDomain,
        
        timeout= timeout,
        userAgent= userAgent,
        outputResults= outputResults,
        threats= threats,
        delay= delay,
        
        hideHTTPCodes= hideHTTPCodes,
        avaliableHTTPCodes= avaliableHTTPCodes,
        hideCharacters= hideCharacters,
        avaliableCharacters= avaliableCharacters,
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
    )