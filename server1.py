import socket              
import json
import datetime
s = socket.socket()         
host = '0.0.0.0' 
port = 12345         


print('Server started!')
print('Waiting for clients...')

s.bind((host, port))
s.listen(5)              
c, addr = s.accept()
print('Got connection from', addr)
while True:
   z = c.recv(1024)
   z.decode('utf-8')
   print(addr, ' >> ', z)
   z=z.decode()
   json_acceptable_string = z.replace("'", "\"")
   z = json.loads(json_acceptable_string)
   with open('CL2.json','w') as file:
      json.dump(z, file)
   with open('CL2.json','r') as file:
      z = json.load(file)
   tmp = z['Timestamp']
   Timestamp=datetime.datetime.now().isoformat(timespec='microseconds')
   z['Timestamp'] = Timestamp
   with open('CL2.json','w') as file:
      json.dump(z, file)
   with open('CL2.json','r') as file:
      z = json.load(file)
   z=str(z)
   z = z.encode()
   print(z)
   c.send(z);

c.close()