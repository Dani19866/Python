# Own modules
from Utilities.SQLInyection.work_w_deepfind import extract_status200, extract_URLRoot
from Utilities.SQLInyection.utils import *
from Utilities.Request.utils import extract_wordlist

# Default modules
from simple_colors import *
import requests
from bs4 import BeautifulSoup

"""
    To construct:
    
    1-. SQL Inyection with DeepFind
    2-. SQL Inyection with Normal Attack (URL)
    3-. Check payload request
    4-. SQL Dump with URL and PARAMS
    5-. SQL Inyection with proxies ===> sendRequest()
    
    Details:
    
    1-. SQL Inyection with DeepFind
        DeepFind return a Array of all URL's with possible attack
        With this Array, find a URL's with forms in her HTML Code and put in other Array
        With this new Array, send request with params (This params has a payload
                                            For example: Have 500 payload
                                                         The query has 5 params
                                                         
                                                         The result is 500 x 5 = 2500 try's
                                            )
                                            
    2-. SQL Inyection with Normal Attack (URL)
        This work with ['URL', 'QUERY', 'METHOD'] in the init function
        With this, start the sql inyection with the diccionary of payloads
    
    3-. Check payload request
        This function is to check the request:
                                        - Status code
                                        - Lenght of code
                                        - Check if return data
                                        - READY: Check timeout (For inyection of time)
                                        - Check if return replaces: <test> to &lt;test&lt;
                                        - READY: Blind SQL Inyection
                                        
                                        The most importa: Check if payload WORK
                                        
"""

# WORK WITH check_response()


class SQLInyection():
    def __init__(
        self,
        # NORMAL ATTACK
        url,
        get,
        post,
        query,

        # DeepFind ATTACK
        deepfind,

        # Header and Cookies
        headers,
        cookies,

    ) -> None:
        # ----------------------------------------------------------------------------------------
        # Init print
        self.prints_verified("Starting SQL Inyection...")

        # ----------------------------------------------------------------------------------------
        # Automatic variables
        self.viewHTML_Request = False
        self.viewMostStatus_Request = {}
        
        self.min_Request = 20
        self.commonResponse_Request = None

        # ----------------------------------------------------------------------------------------
        # General variables
        self.headers = headers if headers is not None else ""
        self.headersQuery = {}
        self.cookies = cookies if cookies is not None else ""
        self.cookiesQuery = {}
        self.diccionaryPayloads = []
        self.diccionaryPATH = [
            # 1-. Common errors
            r"C:\KrakenTools\KrakenInyection\Utilities\Diccionaries\SQLInyection\Inyection\1_mostErrors.txt",

            # 2-. For timeout
            r"C:\KrakenTools\KrakenInyection\Utilities\Diccionaries\SQLInyection\Inyection\2_timeout.txt",

            # 3-. Error based
            r"C:\KrakenTools\KrakenInyection\Utilities\Diccionaries\SQLInyection\Inyection\3_errorBased.txt",

            # 4-. Union select
            r"C:\KrakenTools\KrakenInyection\Utilities\Diccionaries\SQLInyection\Inyection\4_unionSelect.txt",

            # 5-. Bypass Auth
            r"C:\KrakenTools\KrakenInyection\Utilities\Diccionaries\SQLInyection\Inyection\5_bypassAuth.txt",

            # XX-. Etc
            r"C:\KrakenTools\KrakenInyection\Utilities\Diccionaries\SQLInyection\Inyection\99_alls.txt",
        ]

        # ----------------------------------------------------------------------------------------
        # Prevent errors
        if url != None and deepfind == True:
            self.prints_error(
                "Not it possible attack with ['-sqlDP'] and ['-u'] at the same time!")

        if get == True and post == True:
            self.prints_error(
                "Not is possible attack with ['-get'] and ['-post'] at the same time!")

        # ----------------------------------------------------------------------------------------
        # Headers, Cookies and Payloads
        self.headers_cookies_payloads()

        # ----------------------------------------------------------------------------------------
        # Identify attack
        if deepfind:
            self.start_DeepFind()
        else:
            self.start_NormalAttack(url=url, get=get, post=post, query=query)

    # ----------------------------------------------------------------------------------------
    # Attack with Deep Find
    def start_DeepFind(self):
        self.prints_verified("SQL Inyection with DeepFind elected...")
        pass

    # ----------------------------------------------------------------------------------------
    # Normal Attack
    def start_NormalAttack(self, url: str, get: str, post: str, query: dict):
        self.prints_verified("Normal attack elected...")

        # Check URL
        if checkURL(url) == False:
            self.prints_error(
                "Check the URL please, If it blank or not have HTTP or HTTPS")
        else:
            self.prints_verified("URL Verified...")

        # Ready query
        if query == None:
            self.prints_error("Has ocurred a error with a query param")
        else:
            query = checkQuery(query)
            self.prints_verified("Query Verified...")

        # Check method
        if get == True:
            for key, value in query.items():
                if value == "*":
                    for payloadArray in self.diccionaryPayloads:
                        for payload in payloadArray:
                            p = {key: payload}
                            query.update(p)

                            response = self.sendRequest(
                                # General
                                url=url,
                                headers=self.headersQuery,
                                cookies=self.cookiesQuery,

                                # Payload
                                query=query,
                                payload=payload,

                                # Method
                                method="get"
                            )

                            self.checkResponses(response, payload)

        if post == True:
            for key, value in query.items():
                if value == "*":
                    for payloadArray in self.diccionaryPayloads:
                        for payload in payloadArray:
                            p = {key: payload}
                            query.update(p)

                            response = self.sendRequest(
                                # General
                                url=url,
                                headers=self.headersQuery,
                                cookies=self.cookiesQuery,

                                # Payload
                                query=query,
                                payload=payload,

                                # Method
                                method="get"
                            )

                            self.checkResponses(response, payload)

    # ----------------------------------------------------------------------------------------
    # Utils
    def prints_results(self, param: str):
        print(f"{blue('CHECK THIS PAYLOAD:')} {magenta(param)}")

    def prints_verified(self, param: str):
        print(f"{green('VERIFIED:')} {yellow(param)}")

    def prints_error(self, param: str):
        exit(f"{red('[-] ERROR:')} {yellow(param)}")

    def headers_cookies_payloads(self):
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

        # Payloads
        for path in self.diccionaryPATH:
            self.diccionaryPayloads.append(open(path, "r").read().split("\n"))

        self.prints_verified("Cookies, Headers and Payloads READY")

    # ----------------------------------------------------------------------------------------
    def sendRequest(self, url, headers, cookies, query, method, payload):
        if method == "get":
            try:
                response = requests.get(
                    # General
                    url=url,
                    headers=headers,
                    cookies=cookies,

                    # Timeout
                    timeout=4,

                    # Payload
                    params=query
                )

                return response

            except requests.exceptions.Timeout:
                self.prints_results(
                    f"Request: ¿Error in timeout? Payload: {payload}")
            except requests.exceptions.TooManyRedirects:
                self.prints_error(
                    "Request: TOO MANY REDIRECTS. Please check the code")
            except requests.exceptions.SSLError:
                self.prints_error(
                    "Request: ERROR IN SSL CERTIFIED. Please check the code")
            except requests.exceptions.InvalidHeader:
                self.prints_error("Request: ERROR, INVALID HEADER")
            except requests.exceptions.ConnectionError:
                self.prints_error(
                    f"Request: ¿Error in connection? Payload: {payload}")
            except requests.exceptions.RequestException:
                self.prints_error(
                    f"Request: ¿RequestException? Please check the code. Payload: {payload}")

        elif method == "post":
            try:
                response = requests.post(
                    # General
                    url=url,
                    headers=headers,
                    cookies=cookies,

                    # Timeout
                    timeout=4,

                    # Payload
                    params=query
                )

                return response

            except requests.exceptions.Timeout:
                self.prints_results(
                    f"Request: ¿Error in timeout? Payload: {payload}")
            except requests.exceptions.TooManyRedirects:
                self.prints_error(
                    "Request: TOO MANY REDIRECTS. Please check the code")
            except requests.exceptions.SSLError:
                self.prints_error(
                    "Request: ERROR IN SSL CERTIFIED. Please check the code")
            except requests.exceptions.InvalidHeader:
                self.prints_error("Request: ERROR, INVALID HEADER")
            except requests.exceptions.ConnectionError:
                self.prints_error(
                    f"Request: ¿Error in connection? Payload: {payload}")
            except requests.exceptions.RequestException:
                self.prints_error(
                    f"Request: ¿RequestException? Please check the code. Payload: {payload}")

        else:
            self.prints_error("Error in sendRequest() function")

    # ----------------------------------------------------------------------------------------
    # Check responses
    def checkResponses(self, response, payload):
        status = response.status_code
        html = response.text
        lenght = len(extract_wordlist(BeautifulSoup(html, "html.parser")))

        # View if the request is good
        if self.viewHTML_Request == False:
            self.viewHTML_Request = True
            f = open("Results/checkRequest.html", "w", encoding="utf-8")
            f.write(html)
            f.close()
            self.prints_verified(
                "Created checkRequest.html file in /Results/ to confirm the request sent")

        # Note if there is a new response code
        if status not in self.viewMostStatus_Request:
            self.viewMostStatus_Request[status] = 1

        # Note how many times this code was repeated.
        if status in self.viewMostStatus_Request:
            self.viewMostStatus_Request[status] = self.viewMostStatus_Request[status] + 1
            
        # BLIND SQL INYECTION
        # Note the most common response status. This is for [[verify Blind SQL Inyection]]
        if self.commonResponse_Request == None:
            for index in self.viewMostStatus_Request:
                if self.viewMostStatus_Request[index] == self.min_Request:
                    self.commonResponse_Request = index
                    self.prints_verified(f"Most common status response is: {self.commonResponse_Request}")
        if self.commonResponse_Request != None:
            if status != self.commonResponse_Request:
                self.prints_results(f"REASON: different status response, possible BLIND SQL INYECTION. Common: {self.commonResponse_Request} Request: {status} Payload: {payload}")
            
        
        print(f"Status: {status} Lenght: {lenght} Payload: {payload}")