<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
import re
        
def proxyUtility():
    url = "https://free-proxy-list.net"
    proxies = {}

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    container_div = soup.find("tbody")
    box_content = container_div.find_all("td")

    # pass in 0. pass in 1. pass in 2
    # In 8. restart in 0
    count = 0
    countTotalProxies = 0
    temp = []

    for item in box_content:
        # IP
        if ( count == 0 ):
            item = str(item)
            item = re.sub("<td>", "", item)
            item = re.sub("</td>", "", item)
            temp.append(item)
        
        # PORT
        if ( count == 1 ):
            item = str(item)
            item = re.sub("<td>", "", item)
            item = re.sub("</td>", "", item)
            temp.append(item)
        
        # Anonymity
        if ( count == 4 ):
            item = str(item)
            item = re.sub("<td>", "", item)
            item = re.sub("</td>", "", item)
            temp.append(item)
            
        # HTTPS: YES | NO
        if ( count == 6 ):
            item = str(item)
            item = re.sub('<td class="hx">', "", item)
            item = re.sub("</td>", "", item)
            temp.append(item)
        
        count = count + 1
        if ( count == 8 ):
            # Restart count in 0
            count = 0
            # Add temp array proxies in oficial array proxies
            proxies[countTotalProxies] = temp
            # Restart temp
            temp = []
            # Count proxies
            countTotalProxies = countTotalProxies + 1
            
=======
import requests
from bs4 import BeautifulSoup
import re
        
def proxyUtility():
    url = "https://free-proxy-list.net"
    proxies = {}

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    container_div = soup.find("tbody")
    box_content = container_div.find_all("td")

    # pass in 0. pass in 1. pass in 2
    # In 8. restart in 0
    count = 0
    countTotalProxies = 0
    temp = []

    for item in box_content:
        # IP
        if ( count == 0 ):
            item = str(item)
            item = re.sub("<td>", "", item)
            item = re.sub("</td>", "", item)
            temp.append(item)
        
        # PORT
        if ( count == 1 ):
            item = str(item)
            item = re.sub("<td>", "", item)
            item = re.sub("</td>", "", item)
            temp.append(item)
        
        # Anonymity
        if ( count == 4 ):
            item = str(item)
            item = re.sub("<td>", "", item)
            item = re.sub("</td>", "", item)
            temp.append(item)
            
        # HTTPS: YES | NO
        if ( count == 6 ):
            item = str(item)
            item = re.sub('<td class="hx">', "", item)
            item = re.sub("</td>", "", item)
            temp.append(item)
        
        count = count + 1
        if ( count == 8 ):
            # Restart count in 0
            count = 0
            # Add temp array proxies in oficial array proxies
            proxies[countTotalProxies] = temp
            # Restart temp
            temp = []
            # Count proxies
            countTotalProxies = countTotalProxies + 1
            
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
    return proxies