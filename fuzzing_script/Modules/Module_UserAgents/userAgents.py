<<<<<<< HEAD
userAgentsList = []

def readtxt():
    with open("./Modules/Module_UserAgents/user-agents.txt","r") as archivo:
        for linea in archivo:
            userAgentsList.append(linea)
        
def userAgents():
    readtxt()
=======
userAgentsList = []

def readtxt():
    with open("./Modules/Module_UserAgents/user-agents.txt","r") as archivo:
        for linea in archivo:
            userAgentsList.append(linea)
        
def userAgents():
    readtxt()
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
    return userAgentsList