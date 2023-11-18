<<<<<<< HEAD
from colorama import Fore, Back, Style

reservedStatus = {
    200: Fore.GREEN + str(200) + Style.RESET_ALL,
    301: Fore.YELLOW + str(301) + Style.RESET_ALL,
    401: Fore.MAGENTA + str(401) + Style.RESET_ALL,
    403: Fore.CYAN + str(403) + Style.RESET_ALL,
    404: Fore.RED + str(404) + Style.RESET_ALL
}

def pprint(url: str, status: int, w_len: int):
    if ( w_len != 0):
        print(url, status, f"                {w_len}")
    else:
        print(url, status, f"                  {w_len}")

# This functions its called for all Threads when send requests
def printResults(url, status_code, words_len):
    check = True
    checkTwo = True
    point = 105
    minPoint = 90
    
    while check:
        var200 = len(url)  # Example: 41, 45, 55, 70

        # Pass: var200 = 102
        if (var200 >= minPoint):
            if( var200 == point ):
                for status in reservedStatus:
                    if ( status_code == status ):
                        # print(f"{status_code} =====> {status} =====> if")
                        pprint(url, reservedStatus[status], words_len)
                        checkTwo = False
                        return
                        
                if (checkTwo):
                    # print(f"{status_code} =====> {status_code} =====> else")
                    pprint(url, status_code, words_len)
                    return
                    
            # Var200 = 94, 123, 124, 112
            if ( var200 >=minPoint and var200<point ):
                url = url + " "
                
            if ( var200 > point ):
                url = url.replace(" ", "", 1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # else:
        #     url = url + "                "
=======
from colorama import Fore, Back, Style

reservedStatus = {
    200: Fore.GREEN + str(200) + Style.RESET_ALL,
    301: Fore.YELLOW + str(301) + Style.RESET_ALL,
    401: Fore.MAGENTA + str(401) + Style.RESET_ALL,
    403: Fore.CYAN + str(403) + Style.RESET_ALL,
    404: Fore.RED + str(404) + Style.RESET_ALL
}

def pprint(url: str, status: int, w_len: int):
    if ( w_len != 0):
        print(url, status, f"                {w_len}")
    else:
        print(url, status, f"                  {w_len}")

# This functions its called for all Threads when send requests
def printResults(url, status_code, words_len):
    check = True
    checkTwo = True
    point = 105
    minPoint = 90
    
    while check:
        var200 = len(url)  # Example: 41, 45, 55, 70

        # Pass: var200 = 102
        if (var200 >= minPoint):
            if( var200 == point ):
                for status in reservedStatus:
                    if ( status_code == status ):
                        # print(f"{status_code} =====> {status} =====> if")
                        pprint(url, reservedStatus[status], words_len)
                        checkTwo = False
                        return
                        
                if (checkTwo):
                    # print(f"{status_code} =====> {status_code} =====> else")
                    pprint(url, status_code, words_len)
                    return
                    
            # Var200 = 94, 123, 124, 112
            if ( var200 >=minPoint and var200<point ):
                url = url + " "
                
            if ( var200 > point ):
                url = url.replace(" ", "", 1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # else:
        #     url = url + "                "
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
