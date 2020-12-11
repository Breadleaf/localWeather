import requests
import subprocess

script = 'powershell.exe "$tmp =Invoke-WebRequest -URI http://myip.dnsomatic.com/ ; $tmp.content"'
url = "https://google.com"


class InternetConnection:

    @staticmethod
    def isConnected():
        try:
            test = requests.get(url, timeout=5)
            return True
        except requests.ConnectionError:
            return False

    @staticmethod
    def getIpAddress():
        if InternetConnection.isConnected():
            return str((subprocess.check_output(script)).decode("utf-8").strip())
        else:
            return False
