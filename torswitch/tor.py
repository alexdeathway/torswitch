import os
import requests
import time
from stem import Signal
from stem.control import Controller
from stem.process import launch_tor_with_config
from torswitch.logger import logger
from stem.util import term
from torswitch.status import TorStatus
from functools import wraps
config=   {
            'ControlPort':'9051',
            'CookieAuthentication':'1',
          }

def print_bootstrap_lines(line):
    if "Bootstrapped " in line:
        print(term.format(line, term.Color.GREEN))

def wrapper(method):
    @wraps(method)
    def _impl(self, *method_args, **method_kwargs):
        if self.session:
                return method(self, *method_args, **method_kwargs)
        else:
            print(f"Start Tor network before intiating {method.__name__}")
    return _impl

class TorProtocol:
    def __init__(self,limit=None,config=config):
        self.limit=limit
        self.ip_bin={}
        self.proxies = {
            'http': 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
             }
        self.config=config     
        self.session=None
        self.current_ip=None
        self.current_tor_ip=None
        self.last_tor_ip=None

    
    def Start(self):
      try:  
            logger.info("starting tor service..")
            self.session=launch_tor_with_config(config=self.config,init_msg_handler=print_bootstrap_lines,)     
      except:
            print(term.format("Stop tor running on system by'sudo service tor stop'",term.Color.RED))
    
    @wrapper
    def CurrentIp(self):
        self.current_ip=str(requests.get('https://api.ipify.org').text)
        return self.current_ip
    
    @wrapper
    def CurrentTorIp(self):
        self.current_tor_ip= requests.get('https://api.ipify.org',proxies=self.proxies).text
        return self.current_tor_ip
    
    @wrapper
    def NewTorIp(self):
        with Controller.from_port(port = 9051) as c:
                c.authenticate()
                c.signal(Signal.NEWNYM)
                self.current_tor_ip = requests.get('https://api.ipify.org', proxies=self.proxies).text
                return self.current_tor_ip

    @wrapper
    def AbsoluteNewTorIp(self):
        self.last_tor_ip=self.current_tor_ip
        while self.last_tor_ip==self.current_tor_ip:
           self.NewTorIp()
        return self.current_tor_ip
    
    @wrapper
    def TorIpRotation(self,delay=0,limit=10):
        logger.info(term.format(f"Current IP:{self.current_tor_ip}", term.Color.BLUE))
        while True and limit:
            self.last_tor_ip=self.current_tor_ip
            self.NewTorIp()
            if self.current_tor_ip==self.last_tor_ip:
                logger.warning(term.format(f"Stayed at:{self.current_tor_ip}", term.Color.RED))
                continue
            logger.info(term.format(f"Jumped to:{self.current_tor_ip}", term.Color.BLUE))
            limit-=1
            time.sleep(delay)
    
    @wrapper
    def Stop(self):
        self.session.kill()
       


if __name__=="__main__":
    test=TorProtocol()
    print("Current ip:{ip}".format(ip=test.CurrentIp()))
    print("Current tor ip:{tor_ip}".format(tor_ip=test.CurrentTorIp()))
    print("current tor absolute new:",test.AbsoluteNewTorIp())
    print("current tor absolute new:",test.AbsoluteNewTorIp())
    test.TorIpRotation()
