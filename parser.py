#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import cgitb
import subprocess
cgitb.enable()

import re
import glob, os

print ("Content-type: text/html\n")

print ("<html>")
print ("<h2>Nginx's ports</h2>")


os.chdir("/etc/nginx/sites-enabled/")
for file in glob.glob("*.conf"):
#     print (file)
     dirdir = "/etc/nginx/sites-enabled/" + file
     conf = open(dirdir)
     pole = []
     for line in conf:
          line = line.rstrip()
          if re.search('listen', line):
            result = re.findall(r'\d{4}', line)
            pole = pole + result
     ir1 = ', '.join(pole)    
     text = file[:file.index('.conf')]#+0]
     print ("<p>" + "<b>" + text + "</b>" + " = " + " ( " + ir1 + " ) " + "</p>")


print ("</html>")

