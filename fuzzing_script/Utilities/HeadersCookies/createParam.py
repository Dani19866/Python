<<<<<<< HEAD
import re
def headers(param):
    payload = param.headers.split(",")
    payloadDict = {}
    
    for x in payload: 
        titleHead = x
        contentHead = x
        # FOR EXAMPLE: XSS-PROTECTION=1
        # Before =
        titleHead = re.sub(" ", "", titleHead) 
        titleHead = re.search(".{1,}=", titleHead) 
        titleHead = re.sub("=", "", titleHead.group())
        

        # After =
        contentHead = re.search("=.{1,}", contentHead) 
        contentHead = re.sub("=", "", contentHead.group())
        
        # Add data into dict
        payloadDict[titleHead] = contentHead
        
        
    return payloadDict

def cookies(param):
    payload = param.cookies.split(",")
    payloadDict = {}
    
    for x in payload: 
        tittleCookie = x
        contentCookie = x
        # FOR EXAMPLE: XSS-PROTECTION=1
        # Before =
        tittleCookie = re.sub(" ", "", tittleCookie) 
        tittleCookie = re.search(".{1,}=", tittleCookie) 
        tittleCookie = re.sub("=", "", tittleCookie.group())
        

        # After =
        contentCookie = re.search("=.{1,}", contentCookie) 
        contentCookie = re.sub("=", "", contentCookie.group())
        
        # Add data into dict
        payloadDict[tittleCookie] = contentCookie
        
=======
import re
def headers(param):
    payload = param.headers.split(",")
    payloadDict = {}
    
    for x in payload: 
        titleHead = x
        contentHead = x
        # FOR EXAMPLE: XSS-PROTECTION=1
        # Before =
        titleHead = re.sub(" ", "", titleHead) 
        titleHead = re.search(".{1,}=", titleHead) 
        titleHead = re.sub("=", "", titleHead.group())
        

        # After =
        contentHead = re.search("=.{1,}", contentHead) 
        contentHead = re.sub("=", "", contentHead.group())
        
        # Add data into dict
        payloadDict[titleHead] = contentHead
        
        
    return payloadDict

def cookies(param):
    payload = param.cookies.split(",")
    payloadDict = {}
    
    for x in payload: 
        tittleCookie = x
        contentCookie = x
        # FOR EXAMPLE: XSS-PROTECTION=1
        # Before =
        tittleCookie = re.sub(" ", "", tittleCookie) 
        tittleCookie = re.search(".{1,}=", tittleCookie) 
        tittleCookie = re.sub("=", "", tittleCookie.group())
        

        # After =
        contentCookie = re.search("=.{1,}", contentCookie) 
        contentCookie = re.sub("=", "", contentCookie.group())
        
        # Add data into dict
        payloadDict[tittleCookie] = contentCookie
        
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
    return payloadDict