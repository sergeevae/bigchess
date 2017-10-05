#!/usr/bin/env python3

import sys, codecs, os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("Content-type: text/html\n")


#print(os.getcwd())
#os.chdir('C:/Users/sergeevae/Desktop/che')


import pandas as pd

Place = pd.read_csv('cgi-bin/data/Place.csv', header=None, sep=';')
Pieces = pd.read_csv('cgi-bin/data/Pieces.csv', header=None,index_col=0, sep=';')

blen = len(Place.columns)
bh = len(Place.index)

htmlboard=''

print(open('cgi-bin/data/head.html').read())

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
		p_id = piece + str(row+1) + '_' + str(col+1)

		codepart = '<div id="' + p_id + '" class="' + pcolor + '">' + codepiece + '</div>'
		htmlboard = htmlboard + codepart

htmlboard = htmlboard + '</div>'
print(htmlboard)

print('<script>')
print(open('cgi-bin/legalmove.js').read())
print(open('cgi-bin/chess.js').read())
print('</script>')

print('\r\n</body></html>')
