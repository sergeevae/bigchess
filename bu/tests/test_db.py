from tinydb import TinyDB, Query
db = TinyDB('test.json')
db.purge()

db.insert({'type': 'apple', 'count': 7})
db.insert({'type': 'peach1', 'count': 4})


print(db.all())