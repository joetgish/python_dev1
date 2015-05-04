# 4 May 2015
# Joe Welch
# Python 2.7
# Program used to develop baseline for workshop to introduce
# Python, GitHub, collective work
#
# Dev notes:
# 
# 5/4/2015 
# Utility file to begin workshop on developing web resources in Python


# ______________________________________________________
import urllib2

def getPageHTML(urlString):
  response = urllib2.urlopen(urlString)
  html = response.read()

def main():
	print getPageHTML("http://www.google.com" )



if __name__ == '__main__':
	main()


