#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgitb
import os
import re
#import cgi
cgitb.enable()    
#import locale; locale.getlocale()
#sss = os.system ("sudo nginx.py")
#sss = "nginx.py"
print ("Content-type: text/html\n")
print ("""
<html>
<meta charset="utf-8">
<h1>Auto deploy</h1>
<form name="input" action="test.py" method="get">
<input type="submit" value="Deploy">
</form>

<form name="input" action="parser.py" method="get">
<input type="submit" value="Nginx's ports">
</form>
""")

print (""" <form action="nginxtest.py" method="POST">""")# % sss)
print ( """
<select name="users">
""")
with open('/etc/passwd', 'r') as f:
    for line in f:
        if re.search("/bin/bash", line) and int(''.join(re.findall('\\d+', line)[0])) >= 1000 :
            result = re.findall(r'\d{4}', line)
            print ("<option value=" + line[:line.find(":")] + " > " + line[:line.find(":")] + "</option>")

#value="c"
#            print ("<input type="submit" value="Send">")

#  <option>asdasd 2</option>
print ("""</select>
<input type="submit" value="Deploy">
</form>
""")

print (""" <form action="mysqltest.py" method="POST">""")# % sss)
print ( """
<select name="users">
""")
with open('/etc/passwd', 'r') as f:
    for line in f:
        if re.search("/bin/bash", line) and int(''.join(re.findall('\\d+', line)[0])) >= 1000 :
            result = re.findall(r'\d{4}', line)
            print ("<option value=" + line[:line.find(":")] + " > " + line[:line.find(":")] + "</option>")

#value="c"
#            print ("<input type="submit" value="Send">")

#  <option>asdasd 2</option>
print ("""</select>
<input type="submit" value="Check">
</form>

</html>
""")

#html = PPP.encode('utf-8')
#html = PPP
#print (PPP)
