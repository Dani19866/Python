<<<<<<< HEAD
# CLI
from CLI.cli import startCLI

# Classes
from Attacks.Brute_Force.brute_wpa_force import Brute_Force_WPA_v1
from Attacks.Brute_Force.brute_force import Brute_Force_WEB_v1
from Attacks.DeepFind.deepfind import DeepFind_v1
from Attacks.SQLInyection.SQLInyection import SQLInyection

# Default modules
import os
from simple_colors import *

if __name__ == "__main__":
    try:
        argsCLI = startCLI()

        if argsCLI.bf_wpa:
            Brute_Force_WPA_v1(
                wifi_name= argsCLI.wifi_name,
                wifi_new_payload= argsCLI.wifi_payload
            )

        elif argsCLI.bf_web:
            Brute_Force_WEB_v1(
                url= argsCLI.url,
                wordlist= argsCLI.payload,
                method= argsCLI.method,
                postData= argsCLI.postQuery,
                modeXMLHTTPRequest= argsCLI.xmlhttp,
                headers= argsCLI.headers,
                cookies= argsCLI.cookies,
                hideStatus= argsCLI.hideStatus,
                hideLenght= argsCLI.hideLenght
            )

        elif argsCLI.deepFind:
            DeepFind_v1(
                url= argsCLI.url
            )
            
        elif argsCLI.sqlinyection:
            SQLInyection(
                url= argsCLI.url,
                deepfind= argsCLI.sqlinyectionDP,
                headers= argsCLI.headers,
                cookies= argsCLI.cookies,
                get= argsCLI.sqlinyectionGET,
                post= argsCLI.sqlinyectionPOST,
                query= argsCLI.query
            )

    except KeyboardInterrupt:
        print(blue("--------------------------------------------------------------------------------------------------------------------------------------------"))
        print(f"{red('[-] ERROR:')} {yellow('Exiting code 1...')}")
        print(blue("--------------------------------------------------------------------------------------------------------------------------------------------"))
        if argsCLI.bf_wpa:
            os.remove("XML")
            
=======
# CLI
from CLI.cli import startCLI

# Classes
from Attacks.Brute_Force.brute_wpa_force import Brute_Force_WPA_v1
from Attacks.Brute_Force.brute_force import Brute_Force_WEB_v1
from Attacks.DeepFind.deepfind import DeepFind_v1
from Attacks.SQLInyection.SQLInyection import SQLInyection

# Default modules
import os
from simple_colors import *

if __name__ == "__main__":
    try:
        argsCLI = startCLI()

        if argsCLI.bf_wpa:
            Brute_Force_WPA_v1(
                wifi_name= argsCLI.wifi_name,
                wifi_new_payload= argsCLI.wifi_payload
            )

        elif argsCLI.bf_web:
            Brute_Force_WEB_v1(
                url= argsCLI.url,
                wordlist= argsCLI.payload,
                method= argsCLI.method,
                postData= argsCLI.postQuery,
                modeXMLHTTPRequest= argsCLI.xmlhttp,
                headers= argsCLI.headers,
                cookies= argsCLI.cookies,
                hideStatus= argsCLI.hideStatus,
                hideLenght= argsCLI.hideLenght
            )

        elif argsCLI.deepFind:
            DeepFind_v1(
                url= argsCLI.url
            )
            
        elif argsCLI.sqlinyection:
            SQLInyection(
                url= argsCLI.url,
                deepfind= argsCLI.sqlinyectionDP,
                headers= argsCLI.headers,
                cookies= argsCLI.cookies,
                get= argsCLI.sqlinyectionGET,
                post= argsCLI.sqlinyectionPOST,
                query= argsCLI.query
            )

    except KeyboardInterrupt:
        print(blue("--------------------------------------------------------------------------------------------------------------------------------------------"))
        print(f"{red('[-] ERROR:')} {yellow('Exiting code 1...')}")
        print(blue("--------------------------------------------------------------------------------------------------------------------------------------------"))
        if argsCLI.bf_wpa:
            os.remove("XML")
            
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
        exit(1)