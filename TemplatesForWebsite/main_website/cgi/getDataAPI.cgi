#!C:/Python/python.exe

import cgi
import getData
import getjson
import htmlTop
import htmlTail


#main Program

if __name__== "__main__":
	try:
		htmlTop.htmlTop()
		
		htmlTail.htmlTail()
	except:
		cgi.print_exception()
