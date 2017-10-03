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
print('<div class="chessboard">')

for row in range(blen):
	for col in range(blen):
		if (row + col) % 2 == 0: pcolor = 'white' 
		else: pcolor = 'black'

		if row < bh: piece = "b" + Place.loc[row, col]
		elif row >= blen - bh: piece = "w" + Place.loc[blen - row - 1, col]
		else: piece = ""

		if piece == '': codepiece='' 
		else: codepiece = '&#' + str(Pieces.ix[piece][1]) + ';'

		codepart = '<div class="' + pcolor + '">' + codepiece + '</div>'
		htmlboard = htmlboard + codepart

print(htmlboard)

print("""

  <script>

    document.onmousedown = function(e) {


      var x = event.clientX, y = event.clientY,
      piece = document.elementFromPoint(x, y);
      if (piece.innerText=="" | (piece.className != 'black' & piece.className != 'white') ) return;
      console.log(piece.innerText);


var mpiece = document.createElement('div');
mpiece.className = 'black'
mpiece.innerText=piece.innerText;
mpiece.style.background='transparent';
piece.innerText=""


      var coords = getCoords(piece);
      var shiftX = e.pageX - coords.left;
      var shiftY = e.pageY - coords.top;

      mpiece.style.position = 'absolute';
      document.body.appendChild(mpiece);
      moveAt(e);

      mpiece.style.zIndex = 1000; // над другими элементами

      function moveAt(e) {
        mpiece.style.left = e.pageX - shiftX + 'px';
        mpiece.style.top = e.pageY - shiftY + 'px';
      }

      document.onmousemove = function(e) {
        moveAt(e);
      };

      document.onmouseup = function() {
        document.onmousemove = null;
        document.onmouseup = null;
      };

    }

    document.ondragstart = function() {
      return false;
    };


    function getCoords(elem) { // кроме IE8-
      var box = elem.getBoundingClientRect();

      return {
        top: box.top + pageYOffset,
        left: box.left + pageXOffset
      };

    }
  </script>
  
	""")
print('\r\n</body></html>')
