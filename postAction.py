#!/usr/bin/env python3

import sys, codecs, time, json, cgi
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


form = cgi.FieldStorage()
action=form.getvalue('action')
print("Content-type: text/html\n")




obj_json = u'{"answer": [42.2], "abs": 42}'
obj = json.loads(obj_json)
print(repr(obj))





if action=="undefined":
	print("Undefined action")
	sys.exit()



print(action)
#text1 = form.getfirst("TEXT_1", "не задано")

#time.sleep(10) 

