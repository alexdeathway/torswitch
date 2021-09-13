import os
import requests
import time
from stem import Signal
from stem.control import Controller
from torswitch import func_status
from stem.process import launch_tor_with_config
from torswitch import torstatus

class TorProtocol:
    def __init__(self,limit=None,):
        self.limit=limit
        self.ip_bin={}
        self.proxies = {
            'http': 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
             }

        self.current_ip=None
        self.current_tor_ip=None
        self.last_tor_ip=None
    
    def Start(self):
       
       torstatus()


    def CurrentIp(self):
        self.current_ip=str(requests.get('https://api.ipify.org').text)
        return self.current_ip
    
    def CurrentTorIp(self):
        self.current_tor_ip= requests.get('https://api.ipify.org',proxies=self.proxies).text
        return self.current_tor_ip
    
    def NewTorIp(self):
        with Controller.from_port(port = 9051) as c:
                c.authenticate()
                c.signal(Signal.NEWNYM)
                self.current_tor_ip = requests.get('https://api.ipify.org', proxies=self.proxies).text
                return self.current_tor_ip

    def AbsoluteNewTorIp(self):
        self.last_tor_ip=self.current_tor_ip
        while self.last_tor_ip==self.current_tor_ip:
           self.NewTorIp()
        return self.current_tor_ip
    
    def TorIpRotation(self,delay=0,limit=10):
        while True and limit:
            self.last_tor_ip=self.current_tor_ip
            self.NewTorIp()
            if self.current_tor_ip==self.last_tor_ip:
                print("Stayed at:",self.current_tor_ip)
                continue
            print("Jumped to:",self.current_tor_ip)
            limit-=1
            time.sleep(delay)
            """
            with Controller.from_port(port = 9051) as c:
                c.authenticate()
                c.signal(Signal.NEWNYM)
                print("Jumped to:",requests.get('https://api.ipify.org', proxies=self.proxies).text)
            """

    def Stop(self):
        os.system('kill $(pgrep tor)')


if __name__=="__main__":
    test=TorProtocol()
    print("Current ip:{ip}".format(ip=test.CurrentIp()))
    print("Current tor ip:{tor_ip}".format(tor_ip=test.CurrentTorIp()))
    print("current tor absolute new:",test.AbsoluteNewTorIp())
    print("current tor absolute new:",test.AbsoluteNewTorIp())
    test.TorIpRotation()
