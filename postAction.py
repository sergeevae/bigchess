#!/usr/bin/env python3

from tinydb import TinyDB, Query
import sys, codecs, time, json, cgi, os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


form = cgi.FieldStorage()
action=form.getvalue('action')
print("Content-type: text/html\n")



"""
obj_json = u'{"answer": [42.2], "abs": 42}'
obj = json.loads(obj_json)
print(repr(obj))
"""

#print(form)
#FieldStorage(None, None, [MiniFieldStorage('action', 'newmove'), MiniFieldStorage('color', 'white'), MiniFieldStorage('move', '14_6_11_6'), MiniFieldStorage('piece', 'wp')])


if action=="undefined":
	print("Undefined action")
	sys.exit()


if action=="newmove":
	db = TinyDB('data/current.json')
	db.purge()
	db.insert({'type': 'lastmove', 'color': form.getvalue('color'), 'start': form.getvalue('start'), 'end': form.getvalue('end'), 'piece': form.getvalue('piece') })
	
	db = TinyDB('data/all.json')
	db.insert({'type': 'lastmove', 'color': form.getvalue('color'), 'start': form.getvalue('start'), 'end': form.getvalue('end'), 'piece': form.getvalue('piece') })

	print("OK")
	sys.exit()

if action=="getmove":
	res=''; i=1;
	prevcolor="black"
	if form.getvalue('color') == "black":
		prevcolor = "white"

	while True:
		time.sleep(0.5) 
		db = TinyDB('data/current.json'); q=Query();
		res = db.search( (q.type == 'lastmove') & (q.color == prevcolor) ) 
		if (len(res) > 0) | (i>20): break
		i=i+1
	
	if(len(res) == 0):
		print("None", end="")
	else:
		print( str(res[0]).replace("'", '"'), end="" )
	sys.exit()



#text1 = form.getfirst("TEXT_1", "не задано")


