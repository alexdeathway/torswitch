# Tor Switch (unstable release )
Python package to interact with tor and control IP address rotations.


## installation 
Follow these step for installation and configuration. ([reference guide](https://sylvaindurand.org/use-tor-with-python/))
 - install tor
 

> sudo apt install tor

 - configure torrc file 


>  pip3 install torswitch

## Usage

```python
from  torswitch  import  TorProtocol
 
#Create your network
thisnetwork=TorProtocol()

#start your tor network
thisnetwork.Start()

#for changing your ip use
thisnetwork.NewTorIp()

"""
NewTorIP() just request for new ip, ip maybe or maybe not change
"""

  

#for getting absolute new ip use
thisnetwork.AbsoluteNewTorIp()

  

#for continues ip rotation use
thisnetwork.TorIpRotation(delay=3,limit=12)

"""
delay is to define the time gap(in seconds) between new ip address request.
limit is to define how many time you want to make request,default is 10
"""


#finally to stop tor
thisnetwork.stop()

```

use tor proxy
```python 

import requests
from torswitch import TorProtocol

thisnetwork=TorProtocol()
thisnetwork.Start()

proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

proxy=requests.get('https://api.ipify.org',proxies=proxies).text
print(proxy)
thisnetwork.Stop()

```
