  var cellsClass = ["black","white"]

  function isCell(e) {
    if (cellsClass.indexOf(e.className.split(' ')[0]) == -1) {return 0} else {return 1};
  }

  document.onmousedown = function(e) {


    var x = event.clientX, y = event.clientY,
    piece = document.elementFromPoint(x, y);
    if (piece.innerText=="" | !isCell(piece) ) return;
    //console.log(document.getElementsByTagName("div").length);

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

    function MakeMove(e) {
      var x = event.clientX, y = event.clientY,
      cell = document.elementFromPoint(x, y);
      pieceClass=piece.className.split(' ')[1];
      cell.innerText=mpiece.innerText;
      cell.className=cell.className.split(' ')[0] + ' ' + pieceClass;
      piece.removeClass(pieceClass);
    }

    document.onmousemove = function(e) {
      moveAt(e);
    };

    document.onmouseup = function() {
      document.onmousemove = null;
      document.onmouseup = null;

      if(mpiece=="") return;
      mpiece.style["display"]="none"
      if(IfLegalMove(mpiece)) { MakeMove(mpiece) } else { piece.innerText=mpiece.innerText }

      document.body.removeChild(mpiece);
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
