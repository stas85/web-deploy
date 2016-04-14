#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os.path
import sys
import re
import os, glob
import random
import pwd
import grp
import cgi
import cgitb


id = sys.argv[1]
user = id

#user = "testtest"
group = "www-data" 
dir_nginx = "/etc/nginx/sites-enabled/"
file_template = "/var/www/html/virtual_host.template"
dir_projects = "/data/www/"
projects = ["APICO.API", "APICO.Events", "APICO.SmsController", "APICO.Backend", "APICO.RadiusController", "APICO.SmsSender"]


def func_uid(user):
     uid = pwd.getpwnam(user).pw_uid
     return  uid
def func_gid(group):
     gid = grp.getgrnam(group).gr_gid
     return gid

def func_dir(DIR):
    if os.path.exists(DIR):
        return 
    else:

################ HTML
        sys.exit("is not FOUND" + DIR)



def func_auth(AUTH):
   conf = open('/etc/passwd','r')
   for line in conf:
          line = line.rstrip()
          pattern = re.compile("^" + AUTH)
          if pattern.findall(line):
              return
################   HTML
   sys.exit("not found: " + AUTH + " in /etc/passwd")

func_dir("/etc/passwd")
func_dir("/data/www/")
#func_dir(dir_projects + user)
#func_dir("/data/www/logs/")
func_auth("stas")

def func_ports(confnginx,pattern):
   ports = []
   os.chdir(confnginx)
   for file in glob.glob("*.conf"):
      dirdir = confnginx + file
      conf = open(dirdir)
      pole = []
      for line in conf:
          line = line.rstrip()
          if re.search(pattern, line):
            result = re.findall(r'\d{4}', line)
            pole = pole + result
      ports = ports + pole
   ports.sort()
   return (list(map(int, ports)))

def func_portstemplate(conftemplate, patternports):
    conf = open(conftemplate,'r')
    editports = []
    for line in conf:
          line = line.rstrip()
          pattern = re.compile(patternports)
          stop =  pattern.findall(line)
          editports = editports + stop
    return editports

def func_randomport(startport, endport, confnginx, pattern, use_ports):
  number = func_ports(confnginx,pattern) + use_ports
  i = 1
  while i > 0:
    randomport = random.randint(startport, endport)
    i = 0
    for port in number:
        if randomport != port:
           i = i + 0
        else:
           i = i + 1
  return randomport


#for dictionary nginx vhosts ports
def func_dicnginx(dir_nginx, file_template):
   nginxporttemp = func_portstemplate(file_template,"editport.")
   dicnginx = (dict.fromkeys(nginxporttemp))
   for key in dicnginx.keys():
        use_ports = list(dicnginx.values())
        in_port = func_randomport(8106,8119,dir_nginx,"listen", use_ports)
        dicnginx[key] = in_port
   return dicnginx


#for dictionary xdebug ports
def func_dicxdebug(dir_nginx, file_template):
   xdebugporttemp = func_portstemplate(file_template,"editxdebug.")
   dicxdebug = (dict.fromkeys(xdebugporttemp))
   for key in dicxdebug.keys():
        use_ports = list(dicxdebug.values())
        in_port = func_randomport(5500,5700,dir_nginx,"xdebug.remote_port=", use_ports)
        dicxdebug[key] = in_port
   return dicxdebug

#print (func_dicxdebug(dir_nginx, file_template))
#print (func_dicnginx(dir_nginx, file_template))


replnginx = func_dicnginx(dir_nginx, file_template)
repcdebug = func_dicxdebug(dir_nginx, file_template)
replacements = {}
replacements.update(replnginx)
replacements.update(repcdebug)

if os.path.exists("/var/www/html/virttest2"):
     print ("""<font color="red">dir is exist: nginx conf</font>""")
else:
  with open('/var/www/html/virttest', 'r') as infile, open('/var/www/html/virttest2', 'w') as outfile:
      for line in infile:
          line = line.replace("USERSED", user)
          for src, target in replacements.items():
              line = line.replace(src, str(target))
          outfile.write(line)
  print ("""<font color="green">Created file nginx</font>""")



if os.path.exists(dir_projects + user):
     print ("""<font color="red">dir is exist""" + dir_projects + user + """</font>""")
     sys.exit()
else:
     os.mkdir( dir_projects + user )
#     print (dir_projects + user)
     os.chown( dir_projects + user, func_uid("root"), func_gid(group) )
     for ins in projects:
        path = dir_projects + user + "/" + ins + "_" + user
        os.mkdir( path )
        print ("""<font color="green">Created dir """ + path + """</font>""")
        os.chown( path , func_uid(user), func_gid(group) )











  



























