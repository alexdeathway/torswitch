# Tor Switch ## (alpha release )
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
thisnetwork.TorIpRotation(delay=3)

"""
delay is to define the time gap(in seconds) between new ip address request.
"""


#finally to stop tor
thisnetwork.stop()

```
