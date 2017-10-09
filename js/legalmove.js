
function IfLegalMove(e) {
  var x = event.clientX, y = event.clientY,
  cell = document.elementFromPoint(x, y);
  if(!isCell(cell)) return 0;
  if(playercolor != movecolor) return 0;
return 1;
}
