<<<<<<< HEAD
import Modules.Module_Prints.Errors.URL as error

def url(url: str):
    check = url.lower()
    http = check.find("http://")
    https = check.find("https://")
    kFuzz = url.find("kFuzz")
    
    if (http == 0):
        if (kFuzz != -1):
            return 0
        else:
            error.kfuzzError()

    elif (https == 0):
        if (kFuzz != -1):
            return 0
        else:
            error.kfuzzError()
    else:
        error.urlError()
=======
import Modules.Module_Prints.Errors.URL as error

def url(url: str):
    check = url.lower()
    http = check.find("http://")
    https = check.find("https://")
    kFuzz = url.find("kFuzz")
    
    if (http == 0):
        if (kFuzz != -1):
            return 0
        else:
            error.kfuzzError()

    elif (https == 0):
        if (kFuzz != -1):
            return 0
        else:
            error.kfuzzError()
    else:
        error.urlError()
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
