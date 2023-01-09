from logging import exception
from stem.connection import connect

class TorStatus:
    def check():
        return connect()
   
if __name__ == '__main__':
  if TorStatus.check():
      print("Tor is online")
  else:
    print("offline")