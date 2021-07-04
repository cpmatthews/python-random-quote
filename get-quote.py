#!/data/data/com.termux/files/usr/bin/python

def start():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])

if __name__== "__main__":
 start()
