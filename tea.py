#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()


form = cgi.FieldStorage()

#print ("<p>value of id is: %s</p>" % form)


id = form.getvalue("users")

print ("Content-type: text/html\n\n")
print ("<html><body>")
print ("<p>value of id is: %s</p>" % id)
print ("</body></html>")
