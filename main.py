#-*-coding:utf8;-*-
#qpy:3
#qpy:console

from os import *
from urllib.request import urlopen
import json

def localiser(ip):
  res=json.loads(urlopen("http://freegeoip.net/json/%s" %ip).read().decode())
  for i in res.items():
    print ("{}:{}".format(i[0],i[1])    	
      	
if __name__ == '__main__':
  while True:
    ip=str(input("Entrez l'ip-> "))
    localiser(ip)
