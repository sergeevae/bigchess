import sys, time, os
from tinydb import TinyDB, Query

os.chdir(os.path.dirname(os.path.realpath(__file__)))

res=''
while True:
	db = TinyDB('test.json')
	q=Query()
	res = db.search(q.type == 'peach1') 
	if len(res) > 0: break
	print(1)
	time.sleep(1) 

# TODO: signal to stop thread and wake when new move comes. Needs parent process to handle moves.

print(res)

