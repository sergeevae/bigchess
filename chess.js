
  document.onmousedown = function(e) {


    var x = event.clientX, y = event.clientY,
    piece = document.elementFromPoint(x, y);
    if (piece.innerText=="" | (piece.className != 'black' & piece.className != 'white') ) return;
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
      cell.innerText=mpiece.innerText;
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
