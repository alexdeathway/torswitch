from stem.connection import connect

def torstatus():
    controller = connect()
    if  controller:
      controller.close()
      return True
    return False    

if __name__ == '__main__':
  if torstatus():
      print("Tor is online")