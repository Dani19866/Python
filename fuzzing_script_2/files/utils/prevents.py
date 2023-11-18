<<<<<<< HEAD
from simple_colors import *
import time

def prints_verified(verified: str):
    print(f"{magenta('[+]')} {green(verified)}")
    time.sleep(0.75)
    
def prints_advertisement(url: str):
    verify = url.endswith("/")
    if verify:
        print(f"{magenta('[+]')} {cyan('Starting attack to')} {cyan(url)}")
    else:
        print(f"{magenta('[+]')} {cyan('Starting attack to')} {cyan(url)}{cyan('/')}")
    time.sleep(0.75)

def prints_error(error: str):
    exit(f"{red('[-] ERROR:')} {yellow(error)}")
    
def print_exit(error: str):
=======
from simple_colors import *
import time

def prints_verified(verified: str):
    print(f"{magenta('[+]')} {green(verified)}")
    time.sleep(0.75)
    
def prints_advertisement(url: str):
    verify = url.endswith("/")
    if verify:
        print(f"{magenta('[+]')} {cyan('Starting attack to')} {cyan(url)}")
    else:
        print(f"{magenta('[+]')} {cyan('Starting attack to')} {cyan(url)}{cyan('/')}")
    time.sleep(0.75)

def prints_error(error: str):
    exit(f"{red('[-] ERROR:')} {yellow(error)}")
    
def print_exit(error: str):
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
    exit(f"{red('[-] EXITING...')}")