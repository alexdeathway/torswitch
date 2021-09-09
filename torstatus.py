from stem.connection import connect

def TorStatus():
    controller = connect()
    if  controller:
      controller.close()
      return True
    return False    

if __name__ == '__main__':
  if TorStatus():
      print("Tor is online")