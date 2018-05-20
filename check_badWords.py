import urllib
def read_text() :
	quotes = open('C:\Users\Raouf\Desktop\Udacity\movie_quotes\movie_quotes.txt')
	contents = quotes.read()
	print contents
	quotes.close()
	chek_bad(contents)

def chek_bad(text) :
	connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+text)
	output = connection.read()
	if "true" in output :
		print "alert word "
	else :
		if "false" in output :
			print "clear"
		else :
			print "could not check"		
	
	connection.close()

read_text()	
