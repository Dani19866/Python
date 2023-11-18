<<<<<<< HEAD
import argparse
import textwrap

def startCLI():
    parser = argparse.ArgumentParser(
        # Add data...
    )
    # ----------------------------------------------------------------------------------------
    # Brute Force for WPA Wifi wireless
        # Type: Bool
    parser.add_argument( "-bf_wpa", nargs="?", const=True, default=False )
        
        # Type: Str
    parser.add_argument( "-wifi_name" )
    parser.add_argument( "-wifi_payload" )
    
    # ----------------------------------------------------------------------------------------
    # Brute Force for WEB
        # Type: Bool
    parser.add_argument( "-bf_web", nargs="?", const=True, default=False )
    parser.add_argument( "-cP", "--crackPassword", nargs="?", const=True, default=False )
    
        # Type: Bool
    parser.add_argument( "-xml","--xmlhttp", nargs="?", const=True, default=False  )
    
        # Type: Str
    parser.add_argument( "-m", "--method" )
    parser.add_argument( "-pQ", "--postQuery" )
    parser.add_argument( "-payload" )
    
        # Type: Int
    parser.add_argument( "-hS", "--hideStatus" )
    parser.add_argument( "-hL", "--hideLenght" )
    
    # ----------------------------------------------------------------------------------------
    # DeepFind
        # Type: Bool
    parser.add_argument( "-dP", "--deepFind", nargs="?", const=True, default=False )
    
        # Type: Str
        
    # ----------------------------------------------------------------------------------------
    # SQLInyection
        # Type: Bool
    parser.add_argument( "-sql", "--sqlinyection", nargs="?", const=True, default=False )
    parser.add_argument( "-sqlDP", "--sqlinyectionDP", nargs="?", const=True, default=False )
    parser.add_argument( "-get", "--sqlinyectionGET", nargs="?", const=True, default=False )
    parser.add_argument( "-post", "--sqlinyectionPOST", nargs="?", const=True, default=False )

        
    # ----------------------------------------------------------------------------------------
    # General arguments
    parser.add_argument( "-u", "--url" )
    parser.add_argument( "-hd", "--headers" )
    parser.add_argument( "-ck", "--cookies" )
    parser.add_argument( "-q", "--query" )
        
=======
import argparse
import textwrap

def startCLI():
    parser = argparse.ArgumentParser(
        # Add data...
    )
    # ----------------------------------------------------------------------------------------
    # Brute Force for WPA Wifi wireless
        # Type: Bool
    parser.add_argument( "-bf_wpa", nargs="?", const=True, default=False )
        
        # Type: Str
    parser.add_argument( "-wifi_name" )
    parser.add_argument( "-wifi_payload" )
    
    # ----------------------------------------------------------------------------------------
    # Brute Force for WEB
        # Type: Bool
    parser.add_argument( "-bf_web", nargs="?", const=True, default=False )
    parser.add_argument( "-cP", "--crackPassword", nargs="?", const=True, default=False )
    
        # Type: Bool
    parser.add_argument( "-xml","--xmlhttp", nargs="?", const=True, default=False  )
    
        # Type: Str
    parser.add_argument( "-m", "--method" )
    parser.add_argument( "-pQ", "--postQuery" )
    parser.add_argument( "-payload" )
    
        # Type: Int
    parser.add_argument( "-hS", "--hideStatus" )
    parser.add_argument( "-hL", "--hideLenght" )
    
    # ----------------------------------------------------------------------------------------
    # DeepFind
        # Type: Bool
    parser.add_argument( "-dP", "--deepFind", nargs="?", const=True, default=False )
    
        # Type: Str
        
    # ----------------------------------------------------------------------------------------
    # SQLInyection
        # Type: Bool
    parser.add_argument( "-sql", "--sqlinyection", nargs="?", const=True, default=False )
    parser.add_argument( "-sqlDP", "--sqlinyectionDP", nargs="?", const=True, default=False )
    parser.add_argument( "-get", "--sqlinyectionGET", nargs="?", const=True, default=False )
    parser.add_argument( "-post", "--sqlinyectionPOST", nargs="?", const=True, default=False )

        
    # ----------------------------------------------------------------------------------------
    # General arguments
    parser.add_argument( "-u", "--url" )
    parser.add_argument( "-hd", "--headers" )
    parser.add_argument( "-ck", "--cookies" )
    parser.add_argument( "-q", "--query" )
        
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
    return parser.parse_args()