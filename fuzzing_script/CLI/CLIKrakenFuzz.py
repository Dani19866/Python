<<<<<<< HEAD
import argparse
import textwrap

def loadArguments():
    # INITIALIZER CAPTURE ARGUMENTS IN LINE COMMAND
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            ****************************************
            * WordLists: *Folder, *File, quickHits *
            *    subDomains, find*, apache, nginx  *
            *    reverseProxyInc                   *
            ****************************************
            * enableProxy: Dont required send prox *
            ****************************************
            * threats: Dont have limit of threats  *
            ****************************************
            * cookies/headers: This is the formula *
            *     "cookie=value"                   *
            *     "header=value"                   *
            ****************************************
            '''),
            epilog="KrakenFuzz for Kraken in GitHub"
        
        # description="KrakenFuzz for Kraken in GitHub",
        # usage="-u https://www.google.com/kFuzz -wl quickHits -th 200 -sSSL -eP"
    )

    # PRIMARY DATA // ADD ARGUMENTS TO RECEIVED // Type: String
    # parser.add_argument("-u", "--url", required=True)
    # parser.add_argument("-wl", "--wordlist", required=True)

    # SECUNDARY DATA // LARGE DATA // ADD ARGUMENTS TO RECEIVED // Type: String
    # parser.add_argument("-ck", "--cookies", required=False)
    # parser.add_argument("-hh", "--headers", required=False)
    
    # SECUNDARY DATA // ADD ARGUMENTS TO RECEIVED // Type: String
    # parser.add_argument("-ua", "--userAgent", required=False)
    # parser.add_argument("-hc", "--hideHTTPCodes", required=False)
    # parser.add_argument("-ac", "--avaliableHTTPCodes", required=False)
    # parser.add_argument("-hCh", "--hideCharacters", required=False)
    # parser.add_argument("-aCh", "--avaliableCharacters", required=False)

    # SECUNDARY DATA // ADD ARGUMENTS TO RECEIVED // Type: Bool
    # parser.add_argument("-f", "--followRedirect", required=False, nargs='?', const=True)
    # parser.add_argument("-sSSL", "--skipInsecureSSL", required=False, nargs='?', const=False)
    # parser.add_argument("-eP", "--enableProxy", required=False, nargs='?', const=True)
    # parser.add_argument("-sD", "--subDomain", required=False, nargs='?', const=True)
    # parser.add_argument("-o", "--outputResults", required=False)

    # SECUNDARY DATA // ADD ARGUMENTS TO RECEIVED // Type: Int
    # parser.add_argument("-time", "--timeOut", required=False)
    # parser.add_argument("-th", "--threats", required=False)
    # parser.add_argument("-dl", "--delay", required=False)

    # GLOBAL VARIABLE OF ARGUMENTS
    args = parser.parse_args()

    return args

def cli():
    # ALL ARGUMENTS
    args = loadArguments()

=======
import argparse
import textwrap

def loadArguments():
    # INITIALIZER CAPTURE ARGUMENTS IN LINE COMMAND
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            ****************************************
            * WordLists: *Folder, *File, quickHits *
            *    subDomains, find*, apache, nginx  *
            *    reverseProxyInc                   *
            ****************************************
            * enableProxy: Dont required send prox *
            ****************************************
            * threats: Dont have limit of threats  *
            ****************************************
            * cookies/headers: This is the formula *
            *     "cookie=value"                   *
            *     "header=value"                   *
            ****************************************
            '''),
            epilog="KrakenFuzz for Kraken in GitHub"
        
        # description="KrakenFuzz for Kraken in GitHub",
        # usage="-u https://www.google.com/kFuzz -wl quickHits -th 200 -sSSL -eP"
    )

    # PRIMARY DATA // ADD ARGUMENTS TO RECEIVED // Type: String
    # parser.add_argument("-u", "--url", required=True)
    # parser.add_argument("-wl", "--wordlist", required=True)

    # SECUNDARY DATA // LARGE DATA // ADD ARGUMENTS TO RECEIVED // Type: String
    # parser.add_argument("-ck", "--cookies", required=False)
    # parser.add_argument("-hh", "--headers", required=False)
    
    # SECUNDARY DATA // ADD ARGUMENTS TO RECEIVED // Type: String
    # parser.add_argument("-ua", "--userAgent", required=False)
    # parser.add_argument("-hc", "--hideHTTPCodes", required=False)
    # parser.add_argument("-ac", "--avaliableHTTPCodes", required=False)
    # parser.add_argument("-hCh", "--hideCharacters", required=False)
    # parser.add_argument("-aCh", "--avaliableCharacters", required=False)

    # SECUNDARY DATA // ADD ARGUMENTS TO RECEIVED // Type: Bool
    # parser.add_argument("-f", "--followRedirect", required=False, nargs='?', const=True)
    # parser.add_argument("-sSSL", "--skipInsecureSSL", required=False, nargs='?', const=False)
    # parser.add_argument("-eP", "--enableProxy", required=False, nargs='?', const=True)
    # parser.add_argument("-sD", "--subDomain", required=False, nargs='?', const=True)
    # parser.add_argument("-o", "--outputResults", required=False)

    # SECUNDARY DATA // ADD ARGUMENTS TO RECEIVED // Type: Int
    # parser.add_argument("-time", "--timeOut", required=False)
    # parser.add_argument("-th", "--threats", required=False)
    # parser.add_argument("-dl", "--delay", required=False)

    # GLOBAL VARIABLE OF ARGUMENTS
    args = parser.parse_args()

    return args

def cli():
    # ALL ARGUMENTS
    args = loadArguments()

>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
    return args