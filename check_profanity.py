import urllib
import urllib2

proxy_support = urllib2.ProxyHandler({"http":"http://98.126.23.80:10901"})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

def read_text():
	txt = open('G:\Udacity\movie-quotes\movie_quotes\movie_quotes.txt')
	contents_of_file = txt.read()
	# print contents_of_file
	txt.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	# connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+text_to_check)
	connection = urllib2.urlopen('http://www.google.com')
	# connection = urllib.urlopen('http://www.python.org/')
	output = connection.read()
	# print(output)
	connection.close()
	if 'true' in output:
		print('Profinaty Alert!!')
	elif 'false' in output:
		print('This document has no curse words!')
	else:
		print('Could not scan the document properly.')

# read_text()