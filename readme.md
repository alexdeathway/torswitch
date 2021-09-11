# Tow Switch
Python package to interact with tor and control IP address rotations.


## installation 
Follow these step for installation and configuration. ([reference guide](https://sylvaindurand.org/use-tor-with-python/))
 - install tor
 

> sudo apt install tor

 - configure torrc file 

>  sudo vim /etc/tor/torrc
    

	 (i) Uncomment or simply add 

ControlPort 9051
CookieAuthentication 1

>  pip3 install torswitch

## Usage
