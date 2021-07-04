#!/data/data/com.termux/files/usr/bin/python

import random

def start():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[random.randint(len(quotes - 1))])

if __name__== "__main__":
 start()
