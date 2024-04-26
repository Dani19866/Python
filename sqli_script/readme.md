# KrakenInyection: Create by Kraken

Brute Force WPA
----

Init

    python krakenInyection.py -bf_wpa

Wifi name: This start with own payload

    python krakenInyection.py -bf_wpa -wifi_name "wirelessXample"

You payload: This start with your payload

    python krakenInyection.py -bf_wpa -wifi_name "wirelessXample" -wifi_payload "C:/..."


Bruce Force WEB
----

Init

    python krakenInyection.py -bf_web

For GET requests:

    python krakenInyection.py -bf_web -u "https://www.example.com/?q=*" -payload "level_1" -m GET

For POST requests:

    python krakenInyection.py -bf_web -u "https://www.example.com/" -payload "level_1" -m POST -pQ "key=value&crackkey=*"

Request with headers or cookies

    python krakenInyection.py -bf_web -u "https://www.example.com/" -payload "level_1" -m POST -pQ "key=value&crackkey=*" -hd "header1=value1&header2=value2" -ck cookie1=value1&cookie2=value2"

Ignore status code

    python krakenInyection.py -bf_web -u "https://www.example.com/" -payload "level_1" -m POST -pQ "key=value&crackkey=*" -hS 404

Ignore lenght response

    python krakenInyection.py -bf_web -u "https://www.example.com/" -payload "level_1" -m POST -pQ "key=value&crackkey=*" -hL 24

DeepFind
----
If you want to know roots of page (target), you can up this attack to know all of subpages. This is used between SQLInyection, because it
has a function to search in each of all of output.txt. This search a form to try sqlinyection (This is only to status 200 OK in the output)

Init

    python krakenInyection.py -dP -u "https://www.example.com"

SQLInyection
----
words to write...

Init if the target is a URL

    python krakenInyection.py -sql -u "https://www.example.com/" -get|-post -q "query=*&query2=pass"

Only attack 1 param. If you finish the attack with query, start other attack with query2

=======
# KrakenInyection: Create by Kraken

Brute Force WPA
----

Init

    python krakenInyection.py -bf_wpa

Wifi name: This start with own payload

    python krakenInyection.py -bf_wpa -wifi_name "wirelessXample"

You payload: This start with your payload

    python krakenInyection.py -bf_wpa -wifi_name "wirelessXample" -wifi_payload "C:/..."


Bruce Force WEB
----

Init

    python krakenInyection.py -bf_web

For GET requests:

    python krakenInyection.py -bf_web -u "https://www.example.com/?q=*" -payload "level_1" -m GET

For POST requests:

    python krakenInyection.py -bf_web -u "https://www.example.com/" -payload "level_1" -m POST -pQ "key=value&crackkey=*"

Request with headers or cookies

    python krakenInyection.py -bf_web -u "https://www.example.com/" -payload "level_1" -m POST -pQ "key=value&crackkey=*" -hd "header1=value1&header2=value2" -ck cookie1=value1&cookie2=value2"

Ignore status code

    python krakenInyection.py -bf_web -u "https://www.example.com/" -payload "level_1" -m POST -pQ "key=value&crackkey=*" -hS 404

Ignore lenght response

    python krakenInyection.py -bf_web -u "https://www.example.com/" -payload "level_1" -m POST -pQ "key=value&crackkey=*" -hL 24

DeepFind
----
If you want to know roots of page (target), you can up this attack to know all of subpages. This is used between SQLInyection, because it
has a function to search in each of all of output.txt. This search a form to try sqlinyection (This is only to status 200 OK in the output)

Init

    python krakenInyection.py -dP -u "https://www.example.com"

SQLInyection
----
words to write...

Init if the target is a URL

    python krakenInyection.py -sql -u "https://www.example.com/" -get|-post -q "query=*&query2=pass"

Only attack 1 param. If you finish the attack with query, start other attack with query2

    python krakenInyection.py -sql -u "https://www.example.com/" -get|-post -q "query=pass&query2=*"