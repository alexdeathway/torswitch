from logging import exception
from stem.connection import connect
from stem.process import launch_tor_with_config

config=   {
            'ControlPort':'9051',
            'CookieAuthentication':'1',
          }

def torstatus():
    controller = connect()
    if  controller:
      controller.close()
      return True
    print("Starting tor with default config...")  
    launch_tor_with_config(config=config)

def func_status(func):
    try:
      if torstatus():
          func()
      raise exception    
    except TypeError:
      print("Looks like tor is not running.")
   
if __name__ == '__main__':
  if torstatus():
      print("Tor is online")