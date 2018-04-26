#-*-coding:utf8;-*-
#utheur:dvidwilly
""" locliser une ip sur freegeoip"""

from os import *
from urllib.request import urlopen
import json

def localiser(ip):
  try:
    res=json.loads(urlopen("http://freegeoip.net/json/%s" %ip).read().decode())
    for i in res.items():
      print ("{}:{}".format(i[0],i[1])    	
  except:
    print("Erreur de localisation")
      	
if __name__ == '__main__':
  while True:
    ip=str(input("Entrez l'ip-> "))
    localiser(ip)
