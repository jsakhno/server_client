import socket   
import time
import json
import datetime
from random import choice

s = socket.socket()         
host = socket.gethostname() 
port = 12345                

print('Connecting to ', host, port)
s.connect((host, port))


def gen_client():
    ID=''
    Timestamp=datetime.datetime.now().isoformat(timespec='microseconds')
    
    lib=['1','2','3','4','5','6','7','8','9','0','a','b','c','d']
    
    while len(ID) !=5:
        ID += choice(lib)
    client ={
        'ID':ID,
        'Timestamp':Timestamp
    }
    return client



def main():
    
    client=gen_client()
    
    with open('CL.json','w') as file:
        json.dump(client, file)

if __name__=='__main__':
    main()

while True:
   msg = input('CLIENT >> ')
   if msg=='close':
    break
   elif msg=='json':
      i=0
      while i<10:
         i=i+1
         time.sleep(1)
         with open('CL.json', 'r') as file:
             confjson = json.load(file)
         z=str(confjson)
         z = z.encode()
         s.send(z)
         msg = s.recv(1024)
         print('SERVER >> ', msg)
   else:
    msg = msg.encode()
    s.send(msg)
    msg = s.recv(1024)
    print('SERVER >> ', msg)
s.close