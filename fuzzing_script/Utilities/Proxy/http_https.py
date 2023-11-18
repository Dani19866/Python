<<<<<<< HEAD
def http(list: list):
    count = 0
    returnList = []
    filterList = []
    
    for x in list:
        # x: is so a number
        for y in list[x]:
            # list[x]: its a array with ip, port, anony, https
            count = count + 1
            
            if ( count == 4 ):
                if ( y == "no" ):
                    filterList.append(list[x])
                    
                count = 0
                
    for array in filterList:
        proxy = f"{array[0]}:{array[1]}"
        returnList.append(proxy)
            
    return returnList

def https(list: list):
    count = 0
    returnList = []
    filterList = []
    
    for x in list:
        # x: is so a number
        for y in list[x]:
            # list[x]: its a array with ip, port, anony, https
            count = count + 1
            
            if ( count == 4 ):
                if ( y == "yes" ):
                    filterList.append(list[x])
                    
                count = 0
                
    for array in filterList:
        proxy = f"{array[0]}:{array[1]}"
        returnList.append(proxy)
            
=======
def http(list: list):
    count = 0
    returnList = []
    filterList = []
    
    for x in list:
        # x: is so a number
        for y in list[x]:
            # list[x]: its a array with ip, port, anony, https
            count = count + 1
            
            if ( count == 4 ):
                if ( y == "no" ):
                    filterList.append(list[x])
                    
                count = 0
                
    for array in filterList:
        proxy = f"{array[0]}:{array[1]}"
        returnList.append(proxy)
            
    return returnList

def https(list: list):
    count = 0
    returnList = []
    filterList = []
    
    for x in list:
        # x: is so a number
        for y in list[x]:
            # list[x]: its a array with ip, port, anony, https
            count = count + 1
            
            if ( count == 4 ):
                if ( y == "yes" ):
                    filterList.append(list[x])
                    
                count = 0
                
    for array in filterList:
        proxy = f"{array[0]}:{array[1]}"
        returnList.append(proxy)
            
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
    return returnList