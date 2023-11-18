<<<<<<< HEAD
# Create by: Kraken
NOTE: --random-useragent is active for default and no is possible work with a specific useragent

Obligatory values
----

-u, --url & -wl, --wordlist

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "/home/wordlist.txt"
    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt"

Secundary values
----

-th, --threads
    How much threads you want? Recomendation: 200-500

-ck, --cookies & -hd, --headers, --data

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -ck "header=value"
    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -ck "header=value&header2=value2"
    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -hd "header=value"
    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -ch "header=value&header2=value2"

--extensions

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" --extensions ".php,.html,.asp"

Tertiary values
----

--random-useragent

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" --random-userAgent

--followRedirect
    Request module have active for default the redirect (301 to 200). In this software, the redirect is false, if you
    can go redirect automatically, call this option

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" --followRedirect

--skipSSL
    Request module have a protection to insecure SSL certificates. This option skip the insecure SSL certification

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" --skipSSL

--randomProxies
    Extract proxies of "https://free-proxy-list.net" and try with all of HTTP/HTTPS

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" --randomProxies

--proxy
    Manual proxy

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" --proxy "https:IP"


Responses
----

-hc, --hideCode & -ac, --avaliableCode

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -hc 404
    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -ac 200

-hl, --hideLenght & -al, --avaliableLenght

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -hl 144
    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -al 2344


Other options
----

--subdomain

    python fuzz.py -u "https://kFuzz.example.com/" -wl "C:/Tools/SecLists/wordlist.txt" --subdomain

--outputResults

    python fuzz.py -u "https://kFuzz.example.com/" -wl "C:/Tools/SecLists/wordlist.txt" --outputResults

--delay
    This function work with 1 thread and the delay in second

    python fuzz.py -u "https://kFuzz.example.com/" -wl "C:/Tools/SecLists/wordlist.txt" --delay 3

NOTES
----

Fuzz Extensions

    Only Fuzz Extensions work with Manual Proxy

Random User-Agents

    Ever fuzz with random User-Agents, if you want to change the User-Agent, change the code

Random Proxies

    Fuzz with random proxies is probable show false status code, please becareful
=======
# Create by: Kraken
NOTE: --random-useragent is active for default and no is possible work with a specific useragent

Obligatory values
----

-u, --url & -wl, --wordlist

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "/home/wordlist.txt"
    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt"

Secundary values
----

-th, --threads
    How much threads you want? Recomendation: 200-500

-ck, --cookies & -hd, --headers, --data

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -ck "header=value"
    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -ck "header=value&header2=value2"
    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -hd "header=value"
    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -ch "header=value&header2=value2"

--extensions

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" --extensions ".php,.html,.asp"

Tertiary values
----

--random-useragent

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" --random-userAgent

--followRedirect
    Request module have active for default the redirect (301 to 200). In this software, the redirect is false, if you
    can go redirect automatically, call this option

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" --followRedirect

--skipSSL
    Request module have a protection to insecure SSL certificates. This option skip the insecure SSL certification

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" --skipSSL

--randomProxies
    Extract proxies of "https://free-proxy-list.net" and try with all of HTTP/HTTPS

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" --randomProxies

--proxy
    Manual proxy

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" --proxy "https:IP"


Responses
----

-hc, --hideCode & -ac, --avaliableCode

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -hc 404
    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -ac 200

-hl, --hideLenght & -al, --avaliableLenght

    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -hl 144
    python fuzz.py -u "https://www.example.com/kFuzz" -wl "C:/Tools/SecLists/wordlist.txt" -al 2344


Other options
----

--subdomain

    python fuzz.py -u "https://kFuzz.example.com/" -wl "C:/Tools/SecLists/wordlist.txt" --subdomain

--outputResults

    python fuzz.py -u "https://kFuzz.example.com/" -wl "C:/Tools/SecLists/wordlist.txt" --outputResults

--delay
    This function work with 1 thread and the delay in second

    python fuzz.py -u "https://kFuzz.example.com/" -wl "C:/Tools/SecLists/wordlist.txt" --delay 3

NOTES
----

Fuzz Extensions

    Only Fuzz Extensions work with Manual Proxy

Random User-Agents

    Ever fuzz with random User-Agents, if you want to change the User-Agent, change the code

Random Proxies

    Fuzz with random proxies is probable show false status code, please becareful
>>>>>>> b5eeba62e5323d4509741493fbad3cc71f725e39
