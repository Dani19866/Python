<<<<<<< HEAD
# Own modules
from Utilities.SQLInyection.work_w_deepfind import extract_status200, extract_URLRoot

# Default modules
from simple_colors import *
import requests
from bs4 import BeautifulSoup

"""
    --------------------------------------------------------------------------------------------------

    1-. Finish function 'Attack':
            This functions its for iterartor a array with all payloads to load to page
            
    2-. Construct a view response function of 'Attack':
            This functions can be view the response of page for payload
            NOTE:
                -Can view if has WAP/WAF
                -Can view if payload dont work
                -Can view the responses of replaces of strings: <> to &lt;

                IMPORTANT: -Can view if payload WORK
    
    --------------------------------------------------------------------------------------------------
    
    1-. Construct function for attack URL with PARAMS
    
    2-. Construct function to load QUERY PARAM
    
    --------------------------------------------------------------------------------------------------

    1-. Construct function to dump database
    
    2-. Work with folder "Dump" in Diccionaries

"""


class SQLInyection():
    def __init__(
        self,
        url,

        # If work with file create by DeepFind
        deepfind,

        # Params
        headers,
        cookies,

        # Methods
        get,
        post
    ) -> None:
        # ----------------------------------------------------------------------------------------
        # Principal variables
        self.url = url

        # Methods
        self.get = get
        self.post = post

        # ----------------------------------------------------------------------------------------
        # Principal variables if init with deepFind
        self.deepfind = deepfind if deepfind is not None else False
        self.actualURL = None
        self.rootURL = None

        # ----------------------------------------------------------------------------------------
        # Secundary params
        # self.headers = headers if headers is not None else ""
        # self.headersQuery = {}
        # self.cookies = cookies if cookies is not None else ""
        # self.cookiesQuery = {}

        # Attacks send
        # self.attackSend = []  # THIS NOT WORK... IGNORE...
        # self.diccionaryPayloads = []
        # self.diccionaryPATH = [
        #     r"C:\KrakenTools\KrakenInyection\Utilities\Diccionaries\SQLInyection\Inyection\file.txt"
        # ]

        # ----------------------------------------------------------------------------------------
        # IGNORE: Automatic variables
        # NOTE: Params that no change
        self.soupRes = None

        # NOTE: Params that change for url
        # Params for attack
        self.method = None
        self.route = None
        self.query = {}

        # Querys temp
        self.inputs = None
        self.selects = None
        self.textArea = None

        # Form for page
        self.form = None

        # ----------------------------------------------------------------------------------------
        # Prevent errors
        # if self.url != None and self.deepfind == True:
        #     self.prints_error(
        #         "Not it possible attack with ['-sqlDP'] and ['-u'] at the same time!")

        # if self.get == True and self.post == True:
        #     self.prints_error(
        #         "Not is possible attack with ['-get'] and ['-post'] at the same time!")
        # # ----------------------------------------------------------------------------------------
        # Firts point: Extract cookies and headers. Read the diccionary payload
        # self.firtsPoint_verify_HeaderCookies()
        self.readDiccionary()

        # ----------------------------------------------------------------------------------------
        # Second point: Know if with DeepFind output.txt or NOT
        if self.deepfind:
            # Extract all links that return status 200 OK
            try:
                links = extract_status200()
                self.rootURL = extract_URLRoot()
            except:
                self.prints_error(
                    "You send a deepFind attack? Please check the output file in Results/...")

            # Try sqlInyection to all links of Array
            for link in links:
                self.sql_DeepFind(link)
                self.deepFind_resetParams()
        else:
            if self.get:
                self.sql_Attack_GET(self.url)
            elif self.post:
                self.sql_Attack_POST(self.url)
            else:
                self.prints_error("Has a error with Method Attack")

    # ----------------------------------------------------------------------------------------
    # Attack with DeepFind
    def sql_DeepFind(self, url: str):
        self.actualURL = url

        # 1-. Send request
        self.deepFind_req()

        # 2-. Find any form. This is configure for 1 form for page
        self.deepFind_findForm()

        # 3-. Find her method and route
        verify = self.deepFind_Method_and_Route()

        if verify:
            # 4-. Find querys
            self.deepFind_filterQuerys()

            # 5-. Save attack for no repeat to the same target
            targetVerify = self.deepFind_noRepeatAttack()

            if True:
                # 6-. Print params attack
                self.deepFind_printAttack()

                # 7-. Send attack
                if self.method.lower() == "get":
                    self.sql_Attack_GET()
                elif self.method.lower() == "post":
                    self.sql_Attack_POST()
            else:
                pass

    # ----------------------------------------------------------------------------------------
    # Attack Methods
    def sql_Attack_GET(self):
        # Attack with deepFind
        if self.deepfind:
            queryAttack = {}

            for index in self.query:
                queryAttack[index] = "Payload"

                for index in self.query:
                    if index not in queryAttack:
                        queryAttack[index] = "pass"

                # Already query
                self.make_payload(query=queryAttack)

                # Reset query payload
                queryAttack = {}

            # */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
            exit()
            # */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # Normal attack
        else:
            pass

    def sql_Attack_POST(self):
        # Attack with deepFind
        if self.deepfind:
            queryAttack = {}

            for index in self.query:
                # q
                queryAttack[index] = "Payload"

                for index in self.query:
                    if index not in queryAttack:
                        queryAttack[index] = "pass"

                # Already query
                self.make_payload(query=queryAttack)

                # Reset query payload
                queryAttack = {}

        # Normal attack
        else:
            pass

    # ----------------------------------------------------------------------------------------
    # Points
    # def firtsPoint_verify_HeaderCookies(self):
    #     # Headers:
    #     temp = self.headers.split("&")
    #     count = 0
    #     tempIndex = None
    #     tempData = None

    #     for x in temp:
    #         x = x.split("=")

    #         for y in x:
    #             if count == 0:
    #                 tempIndex = y
    #                 count = 1

    #             elif count == 1:
    #                 tempData = y
    #                 count = 2

    #         # Add into a dictionary
    #         if count == 2:
    #             self.headersQuery[tempIndex] = tempData
    #             count = 0

    #     # Cookies:
    #     temp = self.cookies.split("&")
    #     count = 0
    #     tempIndex = None
    #     tempData = None

    #     for x in temp:
    #         x = x.split("=")

    #         for y in x:
    #             if count == 0:
    #                 tempIndex = y
    #                 count = 1

    #             elif count == 1:
    #                 tempData = y
    #                 count = 2

    #         # Add into a dictionary
    #         if count == 2:
    #             self.cookiesQuery[tempIndex] = tempData
    #             count = 0

    #     self.prints_verified("Cookies and headers")

    # ----------------------------------------------------------------------------------------
    # # Utilts
    # def prints_verified(self, param: str):
    #     print(f"{green('VERIFIED:')} {yellow(param)}")

    # def prints_error(self, param: str):
    #     exit(f"{red('[-] ERROR:')} {yellow(param)}")

    # def readDiccionary(self):
    #     for path in self.diccionaryPATH:
    #         self.diccionaryPayloads = open(path, "r").read().split("\n")

    # ----------------------------------------------------------------------------------------
    # Only utils for sql_DeepFind()
    def deepFind_req(self):
        # Send request
        res = requests.get(
            url=self.actualURL,
            timeout=20,
            headers=self.headersQuery,
            cookies=self.cookiesQuery
        )

        # Soup form
        self.soupRes = BeautifulSoup(res.text, "html.parser")

    def deepFind_findForm(self):
        self.form = self.soupRes.find_all("form")

    def deepFind_Method_and_Route(self):
        try:
            self.method = self.form[0]["method"]
            route = self.form[0]["action"]

            self.route = self.deepFind_CleanRoute(route)

            return True
        except:
            return False

    def deepFind_CleanRoute(self, route: str):
        if "http" not in route or "https" not in route:
            route = self.rootURL+route

        return route

    def deepFind_filterQuerys(self):
        # Input
        a = self.soupRes.find_all("input")
        for querys in a:
            try:
                if querys["type"] != "submit":
                    self.query[querys["name"]] = "*"
            except:
                self.query[querys["name"]] = "*"

        # Selects
        b = self.soupRes.find_all("select")
        for querys in b:
            self.query[querys["name"]] = "*"

        # TextArea
        c = self.soupRes.find_all("textarea")
        for querys in c:
            self.query[querys["name"]] = "*"

    def deepFind_printAttack(self):
        print(f"""
{red('---------------------------------------------------------------------------------------------------------------------------------------------------------')}
                  
{cyan('URL')}: {yellow(self.actualURL)}
{cyan('URL Root')}: {yellow(self.rootURL)}

{cyan('Method')}: {yellow(self.method)}
{cyan('Route')}: {yellow(self.route)}

{cyan('Query')}: {yellow(self.query)}

{red('---------------------------------------------------------------------------------------------------------------------------------------------------------')}
        """)

    def deepFind_noRepeatAttack(self):
        if self.route not in self.attackSend:
            self.attackSend.append(self.route)
            return True
        else:
            return False

    def deepFind_resetParams(self):
        # IGNORE: Automatic variables
        # NOTE: Params that no change
        self.soupRes = None

        # NOTE: Prams that change for url
        # Params for attack
        self.method = None
        self.route = None
        self.query = {}

        # Querys temp
        self.inputs = None
        self.selects = None
        self.textArea = None

        # Form for page
        self.form = None

    # ----------------------------------------------------------------------------------------
    # SQL Inyection
    def make_payload(self, query: dict):
        for key, value in query.items():
            if value == "Payload":
                for payload in self.diccionaryPayloads:
                    p = {key: payload}
                    query.update(p)
                    self.send_request(query)

    def send_request(self, query: dict):
        res = None

        # Attack with DeepFind
        if self.deepfind:
            if self.method.lower() == "get":
                try:
                    res = requests.get(url=self.route, timeout=20,
                                       headers=self.headersQuery, cookies=self.cookiesQuery)
                    
                except:
                    pass

            elif self.method.lower() == "post":
                res = requests.post(url=self.route, timeout=20,
                                    headers=self.headersQuery, cookies=self.cookiesQuery)

        # Normal Attack
        else:
            pass
=======
# Own modules
from Utilities.SQLInyection.work_w_deepfind import extract_status200, extract_URLRoot

# Default modules
from simple_colors import *
import requests
from bs4 import BeautifulSoup

"""
    --------------------------------------------------------------------------------------------------

    1-. Finish function 'Attack':
            This functions its for iterartor a array with all payloads to load to page
            
    2-. Construct a view response function of 'Attack':
            This functions can be view the response of page for payload
            NOTE:
                -Can view if has WAP/WAF
                -Can view if payload dont work
                -Can view the responses of replaces of strings: <> to &lt;

                IMPORTANT: -Can view if payload WORK
    
    --------------------------------------------------------------------------------------------------
    
    1-. Construct function for attack URL with PARAMS
    
    2-. Construct function to load QUERY PARAM
    
    --------------------------------------------------------------------------------------------------

    1-. Construct function to dump database
    
    2-. Work with folder "Dump" in Diccionaries

"""


class SQLInyection():
    def __init__(
        self,
        url,

        # If work with file create by DeepFind
        deepfind,

        # Params
        headers,
        cookies,

        # Methods
        get,
        post
    ) -> None:
        # ----------------------------------------------------------------------------------------
        # Principal variables
        self.url = url

        # Methods
        self.get = get
        self.post = post

        # ----------------------------------------------------------------------------------------
        # Principal variables if init with deepFind
        self.deepfind = deepfind if deepfind is not None else False
        self.actualURL = None
        self.rootURL = None

        # ----------------------------------------------------------------------------------------
        # Secundary params
        # self.headers = headers if headers is not None else ""
        # self.headersQuery = {}
        # self.cookies = cookies if cookies is not None else ""
        # self.cookiesQuery = {}

        # Attacks send
        # self.attackSend = []  # THIS NOT WORK... IGNORE...
        # self.diccionaryPayloads = []
        # self.diccionaryPATH = [
        #     r"C:\KrakenTools\KrakenInyection\Utilities\Diccionaries\SQLInyection\Inyection\file.txt"
        # ]

        # ----------------------------------------------------------------------------------------
        # IGNORE: Automatic variables
        # NOTE: Params that no change
        self.soupRes = None

        # NOTE: Params that change for url
        # Params for attack
        self.method = None
        self.route = None
        self.query = {}

        # Querys temp
        self.inputs = None
        self.selects = None
        self.textArea = None

        # Form for page
        self.form = None

        # ----------------------------------------------------------------------------------------
        # Prevent errors
        # if self.url != None and self.deepfind == True:
        #     self.prints_error(
        #         "Not it possible attack with ['-sqlDP'] and ['-u'] at the same time!")

        # if self.get == True and self.post == True:
        #     self.prints_error(
        #         "Not is possible attack with ['-get'] and ['-post'] at the same time!")
        # # ----------------------------------------------------------------------------------------
        # Firts point: Extract cookies and headers. Read the diccionary payload
        # self.firtsPoint_verify_HeaderCookies()
        self.readDiccionary()

        # ----------------------------------------------------------------------------------------
        # Second point: Know if with DeepFind output.txt or NOT
        if self.deepfind:
            # Extract all links that return status 200 OK
            try:
                links = extract_status200()
                self.rootURL = extract_URLRoot()
            except:
                self.prints_error(
                    "You send a deepFind attack? Please check the output file in Results/...")

            # Try sqlInyection to all links of Array
            for link in links:
                self.sql_DeepFind(link)
                self.deepFind_resetParams()
        else:
            if self.get:
                self.sql_Attack_GET(self.url)
            elif self.post:
                self.sql_Attack_POST(self.url)
            else:
                self.prints_error("Has a error with Method Attack")

    # ----------------------------------------------------------------------------------------
    # Attack with DeepFind
    def sql_DeepFind(self, url: str):
        self.actualURL = url

        # 1-. Send request
        self.deepFind_req()

        # 2-. Find any form. This is configure for 1 form for page
        self.deepFind_findForm()

        # 3-. Find her method and route
        verify = self.deepFind_Method_and_Route()

        if verify:
            # 4-. Find querys
            self.deepFind_filterQuerys()

            # 5-. Save attack for no repeat to the same target
            targetVerify = self.deepFind_noRepeatAttack()

            if True:
                # 6-. Print params attack
                self.deepFind_printAttack()

                # 7-. Send attack
                if self.method.lower() == "get":
                    self.sql_Attack_GET()
                elif self.method.lower() == "post":
                    self.sql_Attack_POST()
            else:
                pass

    # ----------------------------------------------------------------------------------------
    # Attack Methods
    def sql_Attack_GET(self):
        # Attack with deepFind
        if self.deepfind:
            queryAttack = {}

            for index in self.query:
                queryAttack[index] = "Payload"

                for index in self.query:
                    if index not in queryAttack:
                        queryAttack[index] = "pass"

                # Already query
                self.make_payload(query=queryAttack)

                # Reset query payload
                queryAttack = {}

            # */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
            exit()
            # */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # Normal attack
        else:
            pass

    def sql_Attack_POST(self):
        # Attack with deepFind
        if self.deepfind:
            queryAttack = {}

            for index in self.query:
                # q
                queryAttack[index] = "Payload"

                for index in self.query:
                    if index not in queryAttack:
                        queryAttack[index] = "pass"

                # Already query
                self.make_payload(query=queryAttack)

                # Reset query payload
                queryAttack = {}

        # Normal attack
        else:
            pass

    # ----------------------------------------------------------------------------------------
    # Points
    # def firtsPoint_verify_HeaderCookies(self):
    #     # Headers:
    #     temp = self.headers.split("&")
    #     count = 0
    #     tempIndex = None
    #     tempData = None

    #     for x in temp:
    #         x = x.split("=")

    #         for y in x:
    #             if count == 0:
    #                 tempIndex = y
    #                 count = 1

    #             elif count == 1:
    #                 tempData = y
    #                 count = 2

    #         # Add into a dictionary
    #         if count == 2:
    #             self.headersQuery[tempIndex] = tempData
    #             count = 0

    #     # Cookies:
    #     temp = self.cookies.split("&")
    #     count = 0
    #     tempIndex = None
    #     tempData = None

    #     for x in temp:
    #         x = x.split("=")

    #         for y in x:
    #             if count == 0:
    #                 tempIndex = y
    #                 count = 1

    #             elif count == 1:
    #                 tempData = y
    #                 count = 2

    #         # Add into a dictionary
    #         if count == 2:
    #             self.cookiesQuery[tempIndex] = tempData
    #             count = 0

    #     self.prints_verified("Cookies and headers")

    # ----------------------------------------------------------------------------------------
    # # Utilts
    # def prints_verified(self, param: str):
    #     print(f"{green('VERIFIED:')} {yellow(param)}")

    # def prints_error(self, param: str):
    #     exit(f"{red('[-] ERROR:')} {yellow(param)}")

    # def readDiccionary(self):
    #     for path in self.diccionaryPATH:
    #         self.diccionaryPayloads = open(path, "r").read().split("\n")

    # ----------------------------------------------------------------------------------------
    # Only utils for sql_DeepFind()
    def deepFind_req(self):
        # Send request
        res = requests.get(
            url=self.actualURL,
            timeout=20,
            headers=self.headersQuery,
            cookies=self.cookiesQuery
        )

        # Soup form
        self.soupRes = BeautifulSoup(res.text, "html.parser")

    def deepFind_findForm(self):
        self.form = self.soupRes.find_all("form")

    def deepFind_Method_and_Route(self):
        try:
            self.method = self.form[0]["method"]
            route = self.form[0]["action"]

            self.route = self.deepFind_CleanRoute(route)

            return True
        except:
            return False

    def deepFind_CleanRoute(self, route: str):
        if "http" not in route or "https" not in route:
            route = self.rootURL+route

        return route

    def deepFind_filterQuerys(self):
        # Input
        a = self.soupRes.find_all("input")
        for querys in a:
            try:
                if querys["type"] != "submit":
                    self.query[querys["name"]] = "*"
            except:
                self.query[querys["name"]] = "*"

        # Selects
        b = self.soupRes.find_all("select")
        for querys in b:
            self.query[querys["name"]] = "*"

        # TextArea
        c = self.soupRes.find_all("textarea")
        for querys in c:
            self.query[querys["name"]] = "*"

    def deepFind_printAttack(self):
        print(f"""
{red('---------------------------------------------------------------------------------------------------------------------------------------------------------')}
                  
{cyan('URL')}: {yellow(self.actualURL)}
{cyan('URL Root')}: {yellow(self.rootURL)}

{cyan('Method')}: {yellow(self.method)}
{cyan('Route')}: {yellow(self.route)}

{cyan('Query')}: {yellow(self.query)}

{red('---------------------------------------------------------------------------------------------------------------------------------------------------------')}
        """)

    def deepFind_noRepeatAttack(self):
        if self.route not in self.attackSend:
            self.attackSend.append(self.route)
            return True
        else:
            return False

    def deepFind_resetParams(self):
        # IGNORE: Automatic variables
        # NOTE: Params that no change
        self.soupRes = None

        # NOTE: Prams that change for url
        # Params for attack
        self.method = None
        self.route = None
        self.query = {}

        # Querys temp
        self.inputs = None
        self.selects = None
        self.textArea = None

        # Form for page
        self.form = None

    # ----------------------------------------------------------------------------------------
    # SQL Inyection
    def make_payload(self, query: dict):
        for key, value in query.items():
            if value == "Payload":
                for payload in self.diccionaryPayloads:
                    p = {key: payload}
                    query.update(p)
                    self.send_request(query)

    def send_request(self, query: dict):
        res = None

        # Attack with DeepFind
        if self.deepfind:
            if self.method.lower() == "get":
                try:
                    res = requests.get(url=self.route, timeout=20,
                                       headers=self.headersQuery, cookies=self.cookiesQuery)
                    
                except:
                    pass

            elif self.method.lower() == "post":
                res = requests.post(url=self.route, timeout=20,
                                    headers=self.headersQuery, cookies=self.cookiesQuery)

        # Normal Attack
        else:
            pass
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
