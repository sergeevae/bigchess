import sys, time
from tinydb import TinyDB, Query

while True:
	db = TinyDB('test.json')
	q=Query()
	res = db.search(q.type == 'peach1') 
	if len(res) > 0: break
	time.sleep(1) 

# TODO: signal to stop thread and wake when new move comes. Needs parent process to handle moves.

print(res)