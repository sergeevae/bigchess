//var result_cat = encodeURIComponent(sel_cat);


function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function postAction(a,d){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "postAction.py", true)
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
    xhr.send("action=" + a + "&" + d);
    xhr.onreadystatechange = function (){ 
		if(xhr.readyState == 4 && xhr.status == 200){ 
			console.log(xhr.responseText);
			if(a == "getmove") { handleMove(xhr.responseText) } else { return xhr.responseText };
		} 
	} 
}

function sendMove(a,b){
	var pieceClass=a.className.split(' ')[1];
	if (pieceClass == null) {
		alert("Потерялась фигура");
		return;
	}
	//var move = a.id + "_" + b.id;
	var poststr =  "color=" + playercolor + "&start=" + a.id + "&end=" + b.id + "&piece=" + pieceClass;
	postAction("newmove",poststr)

}

function getMove(){
	postAction("getmove", "color=" + playercolor)
}


function handleMove(res){
	//
	//console.log(res);
	if(res=="None") {
		getMove();
		return;
	}

	var obj = JSON.parse(res);
	alert(obj.type);

	movecolor = invcolor(movecolor);

}


function MakeMove(e) {
  var x = event.clientX, y = event.clientY,
  cell = document.elementFromPoint(x, y),
  pieceClass=piece.className.split(' ')[1];
  sendMove(piece,cell);

  cell.innerText=mpiece.innerText;
  cell.className=cell.className.split(' ')[0] + ' ' + pieceClass;
  piece.className = piece.className.split(' ')[0];
  movecolor = invcolor(movecolor);
  getMove();
}