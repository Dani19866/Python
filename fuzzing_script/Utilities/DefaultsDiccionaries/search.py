<<<<<<< HEAD
# For discovery folders
smallFolder = "./Modules/Module_DefaultsDiccionaries/Folders/small.txt"
mediumFolder = "./Modules/Module_DefaultsDiccionaries/Folders/medium.txt"
bigFolder = "./Modules/Module_DefaultsDiccionaries/Folders/big.txt"

# For discovery subDomains
subDomains = "./Modules/Module_DefaultsDiccionaries/Subdomains/subdomains_110.000.txt"

# For discovery files (NOT NECESARY PUT .php, .html, .js, etc...)
smallFile = "./Modules/Module_DefaultsDiccionaries/Files/small.txt"
mediumFile = "./Modules/Module_DefaultsDiccionaries/Files/medium.txt"
bigFile = "./Modules/Module_DefaultsDiccionaries/Files/big.txt"

# QuickHits ( The probability of hit in this folders its very high )
quickHits = "./Modules/Module_DefaultsDiccionaries/QuickHits/quickhits.txt"

# CMS
findDrupal = "./Modules/Module_DefaultsDiccionaries/CMS/drupal_7.20.txt"
findJoomla = "./Modules/Module_DefaultsDiccionaries/CMS/joombla_3.0.3.txt"
findSAP = "./Modules/Module_DefaultsDiccionaries/CMS/sap.txt"
findWordPress = "./Modules/Module_DefaultsDiccionaries/CMS/wordpress_3.3.1.txt"

# Apache
apache = "./Modules/Module_DefaultsDiccionaries/Apache/apache.txt"

# Nginx
nginx = "./Modules/Module_DefaultsDiccionaries/Nginx/nginx.txt"

# For languagues
dutchFolder = "./Modules/Module_DefaultsDiccionaries/Languagues/dutch.txt"
frenchFolder = "./Modules/Module_DefaultsDiccionaries/Languagues/french.txt"
italianFolder = "./Modules/Module_DefaultsDiccionaries/Languagues/italian.txt"
portugueseFolder = "./Modules/Module_DefaultsDiccionaries/Languagues/portuguese.txt"

# Reverse proxy inconsistencies
ReverseProxyInc = "./Modules/Module_DefaultsDiccionaries/ReverseProxyInconsistencies/reverse-proxy-inconsistencies.txt"

# For KRAKEN
fuzz1 = "./Modules/Module_DefaultsDiccionaries/KRAKEN/fuzz1.txt"
fuzz2 = "./Modules/Module_DefaultsDiccionaries/KRAKEN/fuzz2.txt"
fuzz3 = "./Modules/Module_DefaultsDiccionaries/KRAKEN/fuzz3.txt"
fuzz4 = "./Modules/Module_DefaultsDiccionaries/KRAKEN/fuzz4.txt"


def AnalyzerParam(param):
    match param:
        # Folder
        case "smallFolder":
            return smallFolder

        case "mediumFolder":
            return mediumFolder

        case "bigFolder":
            return bigFolder

        case "dutchFolder":
            return dutchFolder

        case "frenchFolder":
            return frenchFolder

        case "italianFolder":
            return italianFolder

        case "portugueseFolder":
            return portugueseFolder

        # Subdomains
        case "subDomains":
            return subDomains

        # Files
        case "smallFile":
            return smallFile

        case "mediumFile":
            return mediumFile

        case "bigFile":
            return bigFile

        # CMS
        case "findDrupal":
            return findDrupal

        case "findJoomla":
            return findJoomla

        case "findSAP":
            return findSAP

        case "findWordPress":
            return findWordPress

        # Etc
        case "quickHits":
            return quickHits

        case "KRAKEN":
            pass

        case "apache":
            return apache

        case "nginx":
            return nginx

        case "reverseProxyInc":
            return ReverseProxyInc

        # PATH
        case _:
            # In this case, the user put a PATH, and the KrakenFuzz search starting into root
            return param


def readtxt(param: str):
    payloadList = []
    
    with open(param, "r") as archivo:
        for linea in archivo:
            payloadList.append(linea)
    
    return payloadList
=======
# For discovery folders
smallFolder = "./Modules/Module_DefaultsDiccionaries/Folders/small.txt"
mediumFolder = "./Modules/Module_DefaultsDiccionaries/Folders/medium.txt"
bigFolder = "./Modules/Module_DefaultsDiccionaries/Folders/big.txt"

# For discovery subDomains
subDomains = "./Modules/Module_DefaultsDiccionaries/Subdomains/subdomains_110.000.txt"

# For discovery files (NOT NECESARY PUT .php, .html, .js, etc...)
smallFile = "./Modules/Module_DefaultsDiccionaries/Files/small.txt"
mediumFile = "./Modules/Module_DefaultsDiccionaries/Files/medium.txt"
bigFile = "./Modules/Module_DefaultsDiccionaries/Files/big.txt"

# QuickHits ( The probability of hit in this folders its very high )
quickHits = "./Modules/Module_DefaultsDiccionaries/QuickHits/quickhits.txt"

# CMS
findDrupal = "./Modules/Module_DefaultsDiccionaries/CMS/drupal_7.20.txt"
findJoomla = "./Modules/Module_DefaultsDiccionaries/CMS/joombla_3.0.3.txt"
findSAP = "./Modules/Module_DefaultsDiccionaries/CMS/sap.txt"
findWordPress = "./Modules/Module_DefaultsDiccionaries/CMS/wordpress_3.3.1.txt"

# Apache
apache = "./Modules/Module_DefaultsDiccionaries/Apache/apache.txt"

# Nginx
nginx = "./Modules/Module_DefaultsDiccionaries/Nginx/nginx.txt"

# For languagues
dutchFolder = "./Modules/Module_DefaultsDiccionaries/Languagues/dutch.txt"
frenchFolder = "./Modules/Module_DefaultsDiccionaries/Languagues/french.txt"
italianFolder = "./Modules/Module_DefaultsDiccionaries/Languagues/italian.txt"
portugueseFolder = "./Modules/Module_DefaultsDiccionaries/Languagues/portuguese.txt"

# Reverse proxy inconsistencies
ReverseProxyInc = "./Modules/Module_DefaultsDiccionaries/ReverseProxyInconsistencies/reverse-proxy-inconsistencies.txt"

# For KRAKEN
fuzz1 = "./Modules/Module_DefaultsDiccionaries/KRAKEN/fuzz1.txt"
fuzz2 = "./Modules/Module_DefaultsDiccionaries/KRAKEN/fuzz2.txt"
fuzz3 = "./Modules/Module_DefaultsDiccionaries/KRAKEN/fuzz3.txt"
fuzz4 = "./Modules/Module_DefaultsDiccionaries/KRAKEN/fuzz4.txt"


def AnalyzerParam(param):
    match param:
        # Folder
        case "smallFolder":
            return smallFolder

        case "mediumFolder":
            return mediumFolder

        case "bigFolder":
            return bigFolder

        case "dutchFolder":
            return dutchFolder

        case "frenchFolder":
            return frenchFolder

        case "italianFolder":
            return italianFolder

        case "portugueseFolder":
            return portugueseFolder

        # Subdomains
        case "subDomains":
            return subDomains

        # Files
        case "smallFile":
            return smallFile

        case "mediumFile":
            return mediumFile

        case "bigFile":
            return bigFile

        # CMS
        case "findDrupal":
            return findDrupal

        case "findJoomla":
            return findJoomla

        case "findSAP":
            return findSAP

        case "findWordPress":
            return findWordPress

        # Etc
        case "quickHits":
            return quickHits

        case "KRAKEN":
            pass

        case "apache":
            return apache

        case "nginx":
            return nginx

        case "reverseProxyInc":
            return ReverseProxyInc

        # PATH
        case _:
            # In this case, the user put a PATH, and the KrakenFuzz search starting into root
            return param


def readtxt(param: str):
    payloadList = []
    
    with open(param, "r") as archivo:
        for linea in archivo:
            payloadList.append(linea)
    
    return payloadList
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
