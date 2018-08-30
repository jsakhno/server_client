import socket
import threading
import time
import json
import datetime

s = socket.socket()  
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)       
host = '0.0.0.0' 
port = 12345
s.bind((host, port))

class Server():

   def ltc(client, address):
      while True:
         try:
            z = client.recv(1024)
            if z:
               print(z)
               z = z.decode()
               json_acceptable_string = z.replace("'", "\"")
               z = json.loads(json_acceptable_string)
               with open('GS.json','w') as file:
                  json.dump(z, file)
               with open('GS.json','r') as file:
                  z = json.load(file)
               tmp = z['Timestamp']
               Timestamp=datetime.datetime.now().isoformat(timespec='microseconds')
               z['Timestamp'] = Timestamp
               with open('GS.json','w') as file:
                  json.dump(z, file)
               with open('GS.json','r') as file:
                  z = json.load(file)
               z = str(z)
               z = z.encode()
               print(z)
               client.send(z)
            else:
               raise error('Client disconnected')
         except:
            client.close()
            return False


print('Server started!')
print('Waiting for clients...')

if __name__ == "__main__":
   s.listen(5)
   while True:
      client, address = s.accept()
      client.settimeout(60)
      #v=Server()
      threading.Thread(target = Server.ltc, args = (client,address)).start() 


c.close()