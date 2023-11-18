<<<<<<< HEAD
import argparse
import textwrap

def load_parser():
    # Init capture of arguments
    parser = argparse.ArgumentParser(
        formatter_class = argparse.RawDescriptionHelpFormatter,
        description = textwrap.dedent(''''''),
        epilog = "fuzzing of Kraken"
    )
    
    # ----------------------------------------------------------------------------------------
    # Obligatory values
    parser.add_argument("-u", "--url", required=True, type= str)
    parser.add_argument("-wl", "--wordlist", required=True, type= str)
    parser.add_argument("-m", "--method", required=True, type= str)
    
    # ----------------------------------------------------------------------------------------
    # Secundary values
    parser.add_argument("-ck", "--cookies", required=False, nargs='?', default="", type= str)
    parser.add_argument("-hd", "--headers", required=False, nargs='?', default="", type= str)
    parser.add_argument("-th", "--threads", required=False, nargs='?', default=50, type=int)
    parser.add_argument("--extensions", required=False, nargs='?', default="", type=str)
    parser.add_argument("--data", required=False, nargs='?', default="", type= str)
    
    # ----------------------------------------------------------------------------------------
    # Tertiary values
    parser.add_argument("--random-useragent", required=False, nargs="?", const=True, default=False, type= bool)
    parser.add_argument("--followRedirect", required=False, nargs="?", const=True, default=False, type= bool )
    parser.add_argument("--skipSSL", required=False, nargs="?", const=True, default=False, type= bool )
    parser.add_argument("--random-proxies", required=False, nargs="?", const=True, default=False, type= bool )
    parser.add_argument("--proxy", required=False, nargs="?", default={}, type= str)
    
    # ----------------------------------------------------------------------------------------
    # Responses
    parser.add_argument("-hc", "--hidecode", required=False, nargs='?', default=None, type=str)
    parser.add_argument("-hl", "--hidelenght", required=False, nargs='?', default=None, type=str)
    
    parser.add_argument("-ac", "--avaliablecode", required=False, nargs='?', default=None, type=str)
    parser.add_argument("-al", "--avaliablelenght", required=False, nargs='?', default=None, type=str)
    
    # ----------------------------------------------------------------------------------------
    # Other options
    parser.add_argument("--subdomain", required=False, nargs='?', default=False, const=True)
    parser.add_argument("--outputResults", required=False, nargs='?', default=False, const=True)
    parser.add_argument("--delay", required=False, nargs='?', default=False, const=True)

    # ----------------------------------------------------------------------------------------
    # IGNORE: Global variables
    args = parser.parse_args()
=======
import argparse
import textwrap

def load_parser():
    # Init capture of arguments
    parser = argparse.ArgumentParser(
        formatter_class = argparse.RawDescriptionHelpFormatter,
        description = textwrap.dedent(''''''),
        epilog = "fuzzing of Kraken"
    )
    
    # ----------------------------------------------------------------------------------------
    # Obligatory values
    parser.add_argument("-u", "--url", required=True, type= str)
    parser.add_argument("-wl", "--wordlist", required=True, type= str)
    parser.add_argument("-m", "--method", required=True, type= str)
    
    # ----------------------------------------------------------------------------------------
    # Secundary values
    parser.add_argument("-ck", "--cookies", required=False, nargs='?', default="", type= str)
    parser.add_argument("-hd", "--headers", required=False, nargs='?', default="", type= str)
    parser.add_argument("-th", "--threads", required=False, nargs='?', default=50, type=int)
    parser.add_argument("--extensions", required=False, nargs='?', default="", type=str)
    parser.add_argument("--data", required=False, nargs='?', default="", type= str)
    
    # ----------------------------------------------------------------------------------------
    # Tertiary values
    parser.add_argument("--random-useragent", required=False, nargs="?", const=True, default=False, type= bool)
    parser.add_argument("--followRedirect", required=False, nargs="?", const=True, default=False, type= bool )
    parser.add_argument("--skipSSL", required=False, nargs="?", const=True, default=False, type= bool )
    parser.add_argument("--random-proxies", required=False, nargs="?", const=True, default=False, type= bool )
    parser.add_argument("--proxy", required=False, nargs="?", default={}, type= str)
    
    # ----------------------------------------------------------------------------------------
    # Responses
    parser.add_argument("-hc", "--hidecode", required=False, nargs='?', default=None, type=str)
    parser.add_argument("-hl", "--hidelenght", required=False, nargs='?', default=None, type=str)
    
    parser.add_argument("-ac", "--avaliablecode", required=False, nargs='?', default=None, type=str)
    parser.add_argument("-al", "--avaliablelenght", required=False, nargs='?', default=None, type=str)
    
    # ----------------------------------------------------------------------------------------
    # Other options
    parser.add_argument("--subdomain", required=False, nargs='?', default=False, const=True)
    parser.add_argument("--outputResults", required=False, nargs='?', default=False, const=True)
    parser.add_argument("--delay", required=False, nargs='?', default=False, const=True)

    # ----------------------------------------------------------------------------------------
    # IGNORE: Global variables
    args = parser.parse_args()
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
    return args