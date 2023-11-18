<<<<<<< HEAD
# Own modules
from Utilities.DeepFind.rutes import robots
from Utilities.Request.utils import extract_wordlist

# Default modules
import requests
from bs4 import BeautifulSoup
from simple_colors import *

class DeepFind_v1():
    def __init__(
        self,
        url
    ) -> None:
        # ----------------------------------------------------------------------------------------
        # Principal variables
        self.url = url
        self.statusOK = []
        self.statusNOTFOUND = []
        self.statusOTHERS = []
        self.statusForVERIFY = []

        # ----------------------------------------------------------------------------------------
        # Routes
        self.routes = {
            # /robots.txt
            "robots": [],
            "robots_links": [],

            # Pages
            "pages": []
        }

        # ----------------------------------------------------------------------------------------
        # Others
        self.filters = [
            "Sitemap: ",
            "Disallow: ",
        ]

        self.ignoreLines = [
            "#",
            "User-Agent",
            "User-agent",
            "Crawl-Delay",
            "Crawl-delay"
        ]
        self.ignoreLines_number = len(self.ignoreLines)

        self.numers = []

        # ----------------------------------------------------------------------------------------
        # Firts point: URL written correctly
        self.checkURL()

        # ----------------------------------------------------------------------------------------
        # Second point: See /robots.txt
        self.view_robots()
        self.search(self.routes["robots_links"])
        self.search(self.routes["robots"])
        
        # ----------------------------------------------------------------------------------------
        # Third point: See main pages and her roots
        self.view_pages()
        self.search(self.routes["pages"])
        
        # ----------------------------------------------------------------------------------------
        # Last point: Write in a txt file
        self.output()
        
    # ----------------------------------------------------------------------------------------
    # Verify entry of URL
    def checkURL(self):
        if self.url.endswith("/"):
            position = self.url.find("/", 8)
            self.url = self.url[0:position]

        if "http://" in self.url or "https://" in self.url:
            pass
        else:
            self.prints_error("URL param no has HTTP:// or HTTPS://")

    # View robots.txt page
    def view_robots(self):
        res = requests.get(url=self.url+robots, timeout=20)
        lines = res.text.split("\n")
        checkFilter = True
        
        for line in lines:
            # Disallow: /admin ====> /admin
            for filter in self.filters:
                line = line.replace(filter, "")

            # User-agent: Nutch ===> None
            for ignore in self.ignoreLines:
                if ignore in line:
                    checkFilter = False
            
            # If pass all of filters
            if checkFilter:
                if "http" in line or "https" in line:
                    if line not in self.routes["robots_links"]:
                        self.routes["robots_links"].append(line)
                else:
                    if line not in self.routes["robots"]:
                        self.routes["robots"].append(line)
            
            # Reset checkFilter
            checkFilter = True

    # View home page and her roots
    def view_pages(self):
        res = requests.get(url= self.url)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # Search links
        links = soup.find_all("a")
        
        for link in links:
            try:
                
                if "http://" not in link["href"]:
                    if "https://" not in link["href"]:
                        # Filter
                        if "#" in link['href']:
                            pass
                        # Whatsapp numbers
                        elif "whatsapp://" in link['href']:
                            self.numers.append(link['href'])
                        # 
                        else:
                            self.view_roots_pages(link["href"])
                    else:
                        if self.url in link['href']:
                            self.view_roots_pages(link["href"])
                        
                else:
                    if self.url in link['href']:
                        self.view_roots_pages(link["href"])
                    
            except:
                print(f"ERROR IN View_Pages: {link}")
    
    # View home page and her roots
    def view_roots_pages(self, root: str):
        # Filter: routes/robots
        if root in self.routes["robots"]:
            return
        # Filter: routes/robots_links
        elif root in self.routes["robots_links"]:
            return
        # Filter: routes/pages
        elif root in self.routes["pages"]:
            return
        # Added into routes/pages
        else:
            self.routes["pages"].append(root)

    # Output results
    def output(self):
        f = open("Results/DeepFind_output.txt", "w")
        
        f.write("-------------------------------------------------------------------------------------------\n")
        f.write(f"URL ROOT: {self.url}\n")
        
        f.write("-------------------------------------------------------------------------------------------\n")
        f.write("STATUS 200 OK\n")
        for line in self.statusOK:
            f.write(line)
            f.write("\n")
            
        f.write("-------------------------------------------------------------------------------------------\n")
        f.write("STATUS 404 NOT FOUND\n")
        for line in self.statusNOTFOUND:
            f.write(line)
            f.write("\n")
            
        f.write("-------------------------------------------------------------------------------------------\n")
        f.write("STATUS VARIETY\n")
        for line in self.statusOTHERS:
            f.write(line)
            f.write("\n")
            
        f.write("-------------------------------------------------------------------------------------------\n")
        f.write("STATUS FOR VERIFY\n")
        for line in self.statusForVERIFY:
            f.write(line)
            f.write("\n")
        
        f.write("-------------------------------------------------------------------------------------------\n")
        f.write("NUMBERS PHONE\n")
        for line in self.numers:
            f.write(line)
            f.write("\n")
            
        f.write("-------------------------------------------------------------------------------------------") 
        f.close()
        
    # ----------------------------------------------------------------------------------------
    # Utils:
    def search(self, routes: list | dict):
        for route in routes:
            if "http" in route or "https" in route:
                try:
                    self.req(route)
                except:
                    print(f"ERROR IN Search-1: {route}")
            else:
                if "*" not in route:
                    try:
                        self.req(self.url+route)
                    except:
                        print(f"ERROR IN Search-1: {route}")
                    
                else:
                    self.statusForVERIFY.append(route)
    
    def req(self, route: str):
        if route == self.url or route == f"{self.url}/":
            pass
        else:
            res = requests.get(url= route, timeout= 20)
            status = res.status_code
            
            if status == 200:
                self.statusOK.append(route)
            elif status == 404:
                self.statusNOTFOUND.append(route)
            else:
=======
# Own modules
from Utilities.DeepFind.rutes import robots
from Utilities.Request.utils import extract_wordlist

# Default modules
import requests
from bs4 import BeautifulSoup
from simple_colors import *

class DeepFind_v1():
    def __init__(
        self,
        url
    ) -> None:
        # ----------------------------------------------------------------------------------------
        # Principal variables
        self.url = url
        self.statusOK = []
        self.statusNOTFOUND = []
        self.statusOTHERS = []
        self.statusForVERIFY = []

        # ----------------------------------------------------------------------------------------
        # Routes
        self.routes = {
            # /robots.txt
            "robots": [],
            "robots_links": [],

            # Pages
            "pages": []
        }

        # ----------------------------------------------------------------------------------------
        # Others
        self.filters = [
            "Sitemap: ",
            "Disallow: ",
        ]

        self.ignoreLines = [
            "#",
            "User-Agent",
            "User-agent",
            "Crawl-Delay",
            "Crawl-delay"
        ]
        self.ignoreLines_number = len(self.ignoreLines)

        self.numers = []

        # ----------------------------------------------------------------------------------------
        # Firts point: URL written correctly
        self.checkURL()

        # ----------------------------------------------------------------------------------------
        # Second point: See /robots.txt
        self.view_robots()
        self.search(self.routes["robots_links"])
        self.search(self.routes["robots"])
        
        # ----------------------------------------------------------------------------------------
        # Third point: See main pages and her roots
        self.view_pages()
        self.search(self.routes["pages"])
        
        # ----------------------------------------------------------------------------------------
        # Last point: Write in a txt file
        self.output()
        
    # ----------------------------------------------------------------------------------------
    # Verify entry of URL
    def checkURL(self):
        if self.url.endswith("/"):
            position = self.url.find("/", 8)
            self.url = self.url[0:position]

        if "http://" in self.url or "https://" in self.url:
            pass
        else:
            self.prints_error("URL param no has HTTP:// or HTTPS://")

    # View robots.txt page
    def view_robots(self):
        res = requests.get(url=self.url+robots, timeout=20)
        lines = res.text.split("\n")
        checkFilter = True
        
        for line in lines:
            # Disallow: /admin ====> /admin
            for filter in self.filters:
                line = line.replace(filter, "")

            # User-agent: Nutch ===> None
            for ignore in self.ignoreLines:
                if ignore in line:
                    checkFilter = False
            
            # If pass all of filters
            if checkFilter:
                if "http" in line or "https" in line:
                    if line not in self.routes["robots_links"]:
                        self.routes["robots_links"].append(line)
                else:
                    if line not in self.routes["robots"]:
                        self.routes["robots"].append(line)
            
            # Reset checkFilter
            checkFilter = True

    # View home page and her roots
    def view_pages(self):
        res = requests.get(url= self.url)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # Search links
        links = soup.find_all("a")
        
        for link in links:
            try:
                
                if "http://" not in link["href"]:
                    if "https://" not in link["href"]:
                        # Filter
                        if "#" in link['href']:
                            pass
                        # Whatsapp numbers
                        elif "whatsapp://" in link['href']:
                            self.numers.append(link['href'])
                        # 
                        else:
                            self.view_roots_pages(link["href"])
                    else:
                        if self.url in link['href']:
                            self.view_roots_pages(link["href"])
                        
                else:
                    if self.url in link['href']:
                        self.view_roots_pages(link["href"])
                    
            except:
                print(f"ERROR IN View_Pages: {link}")
    
    # View home page and her roots
    def view_roots_pages(self, root: str):
        # Filter: routes/robots
        if root in self.routes["robots"]:
            return
        # Filter: routes/robots_links
        elif root in self.routes["robots_links"]:
            return
        # Filter: routes/pages
        elif root in self.routes["pages"]:
            return
        # Added into routes/pages
        else:
            self.routes["pages"].append(root)

    # Output results
    def output(self):
        f = open("Results/DeepFind_output.txt", "w")
        
        f.write("-------------------------------------------------------------------------------------------\n")
        f.write(f"URL ROOT: {self.url}\n")
        
        f.write("-------------------------------------------------------------------------------------------\n")
        f.write("STATUS 200 OK\n")
        for line in self.statusOK:
            f.write(line)
            f.write("\n")
            
        f.write("-------------------------------------------------------------------------------------------\n")
        f.write("STATUS 404 NOT FOUND\n")
        for line in self.statusNOTFOUND:
            f.write(line)
            f.write("\n")
            
        f.write("-------------------------------------------------------------------------------------------\n")
        f.write("STATUS VARIETY\n")
        for line in self.statusOTHERS:
            f.write(line)
            f.write("\n")
            
        f.write("-------------------------------------------------------------------------------------------\n")
        f.write("STATUS FOR VERIFY\n")
        for line in self.statusForVERIFY:
            f.write(line)
            f.write("\n")
        
        f.write("-------------------------------------------------------------------------------------------\n")
        f.write("NUMBERS PHONE\n")
        for line in self.numers:
            f.write(line)
            f.write("\n")
            
        f.write("-------------------------------------------------------------------------------------------") 
        f.close()
        
    # ----------------------------------------------------------------------------------------
    # Utils:
    def search(self, routes: list | dict):
        for route in routes:
            if "http" in route or "https" in route:
                try:
                    self.req(route)
                except:
                    print(f"ERROR IN Search-1: {route}")
            else:
                if "*" not in route:
                    try:
                        self.req(self.url+route)
                    except:
                        print(f"ERROR IN Search-1: {route}")
                    
                else:
                    self.statusForVERIFY.append(route)
    
    def req(self, route: str):
        if route == self.url or route == f"{self.url}/":
            pass
        else:
            res = requests.get(url= route, timeout= 20)
            status = res.status_code
            
            if status == 200:
                self.statusOK.append(route)
            elif status == 404:
                self.statusNOTFOUND.append(route)
            else:
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
                self.statusOTHERS.append(route)