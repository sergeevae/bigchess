#!/usr/bin/env python3

import sys, codecs, os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("Content-type: text/html\n")


#print(os.getcwd())
#os.chdir('C:/Users/sergeevae/Desktop/che')


import pandas as pd
import datetime
from tinydb import TinyDB

alljson = 'data/all.json'
currentjson = 'data/current.json'
timejson = 'data/games/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S") + '.json'
if os.path.isfile(alljson):
	os.rename(alljson,timejson)

TinyDB('data/current.json').purge()

Place = pd.read_csv('data/Place.csv', header=None, sep=';')
Pieces = pd.read_csv('data/Pieces.csv', header=None,index_col=0, sep=';')

blen = len(Place.columns)
bh = len(Place.index)

htmlboard=''

print(open('data/head.html').read())

print('<body>')
print('<div id="board" class="chessboard"> ')

for row in range(blen):
	for col in range(blen):
		if (row + col) % 2 == 0: pcolor = 'white' 
		else: pcolor = 'black'

		if row < bh: piece = "b" + Place.loc[row, col]
		elif row >= blen - bh: piece = "w" + Place.loc[blen - row - 1, col]
		else: piece = ""

		if piece == '': codepiece='' 
		else: codepiece = '&#' + str(Pieces.ix[piece][1]) + ';'
		c_id = str(blen-row) + '_' + str(col+1)

		if piece == '': 
			codepart = '<div id="' + c_id + '" class="' + pcolor + '">' + codepiece + '</div>'
		else:
			codepart = '<div id="' + c_id + '" class="' + pcolor + ' ' + piece + '">' + codepiece + '</div>'
		htmlboard = htmlboard + codepart

htmlboard = htmlboard + '</div>'
print(htmlboard)

print('<div id="move">Ход</div>')

#print('<script src="../js/jquery-2.2.4.min.js" type="text/javascript"></script>')
#print('<script src="https://code.jquery.com/jquery-2.2.4.min.js" type="text/javascript"></script>')
print('<script src="../data/postAction.js" type="text/javascript"></script>')


print('<script>')
print(open('data/legalmove.js').read())
print(open('data/chess.js').read())
print('</script>')

print('\r\n</body></html>')
