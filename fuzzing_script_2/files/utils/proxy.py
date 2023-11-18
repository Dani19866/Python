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
            
    return proxies

def onlyHTTPS(list: list):
    count = 0
    returnList = []
    filterList = []
    
    for x in list:
        # x: is so a number
        for y in list[x]:
            # list[x]: its a array with ip, port, anony, https
            count = count + 1
            
            if ( count == 4 ):
                # "yes": If have a HTTPS
                if ( y == "yes" ):
                    filterList.append(list[x])
                    
                count = 0
                
    for array in filterList:
        proxy = f"{array[0]}:{array[1]}"
        returnList.append(proxy)
            
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
            
    return proxies

def onlyHTTPS(list: list):
    count = 0
    returnList = []
    filterList = []
    
    for x in list:
        # x: is so a number
        for y in list[x]:
            # list[x]: its a array with ip, port, anony, https
            count = count + 1
            
            if ( count == 4 ):
                # "yes": If have a HTTPS
                if ( y == "yes" ):
                    filterList.append(list[x])
                    
                count = 0
                
    for array in filterList:
        proxy = f"{array[0]}:{array[1]}"
        returnList.append(proxy)
            
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
    return returnList