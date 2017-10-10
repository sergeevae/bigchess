
function IfLegalMove(e) {
  var x = event.clientX, y = event.clientY,
  cell = document.elementFromPoint(x, y);
  if(!isCell(cell)) return 0;
  if(playercolor != movecolor) return 0;
  var piececolor = piece.className.split(' ')[1];
  if(piececolor.substr(0,1) != movecolor.substr(0,1)) return 0;
  if(piece.id == cell.id) return 0;




return 1;
}
