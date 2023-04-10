# Tor Switch

<div align="center">
<img width="300" src="https://github.com/alexdeathway/torswitch/blob/master/assets/logo/ProjectLogo.png"  alt="logo"/>

[![Build and Publish Package](https://github.com/alexdeathway/torswitch/actions/workflows/build%20&%20publish.yaml/badge.svg)](https://github.com/alexdeathway/torswitch/actions/workflows/build%20&%20publish.yaml)
[![Python Package Test](https://github.com/alexdeathway/torswitch/actions/workflows/test.yaml/badge.svg)](https://github.com/alexdeathway/torswitch/actions/workflows/test.yaml)
[![PyPI version](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=PyPI&query=$.info.version&url=https://pypi.org/pypi/torswitch/json)](https://pypi.org/project/torswitch/) [![License](https://img.shields.io/github/license/alexdeathway/torswitch.svg)](https://github.com/alexdeathway/torswitch/blob/main/LICENSE)


</div>

Python package to interact with tor and control IP address rotations.

## Installation 
 - install tor
 
 > sudo apt install tor

 - install torswitch

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

## Use tor as proxy
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
--- 
