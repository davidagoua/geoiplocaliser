#-*-coding:utf8;-*-
#autheur:dvidwilly
""" locliser une ip sur freegeoip"""

import os
from request import get
import json
import sys
             

def localiser(ip):
  try:
    res = json.load(get('http://ipstack./json/%s', %ip).read.decode())
    for key, val in res.items():
      print("{} : {} ".format(key, val))
      except:
        print("Erreur dans le chargement de l'api")
 
if __name__ == '__main__':
  localiser(sys.argv[1])
