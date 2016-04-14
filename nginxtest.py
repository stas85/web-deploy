#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os.path
import sys
import re
import os, glob
import subprocess
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

id = form.getvalue("users")
#id= "testtest"
print ("Content-type: text/html\n\n")
print ("<html><body>")

def run():    
    popen = subprocess.Popen(['sudo','python3','/var/www/html/nginx.py', id], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return iter(popen.stdout.readline, b"")

for line in run():
    print("<p>")
    print(line.decode('ascii'))
    print("</p>")

#print("<p><font color="red">This is some text!</font></p>")

print ("</body></html>")
