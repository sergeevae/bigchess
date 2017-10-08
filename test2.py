#!/usr/bin/env python3

import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")

print("<script>")
print(open('cgi-bin/postAction.js').read())
print("</script>")



print("<body>")
print("<h2>Hello %s %s</h2>" % (first_name, last_name) )
print("</body>")
print("</html>")