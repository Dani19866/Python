def checkURL(url: str):
    check = url.lower()
    http = check.find("http://")
    https = check.find("https://")

    if http == 0:
        return True
    elif https == 0:
        return True
    else:
        return False
    
def checkQuery(query: str):
    returnQuery = {}
    
    # Query:
    temp = query.split("&")
    count = 0
    tempIndex = None
    tempData = None

    for x in temp:
        x = x.split("=")

        for y in x:
            if count == 0:
                tempIndex = y
                count = 1

            elif count == 1:
                tempData = y
                count = 2

        # Add into a dictionary
        if count == 2:
            returnQuery[tempIndex] = tempData
            count = 0
            
    return returnQuery