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
	if(res=="None") {
		getMove();
		return;
	}

	var obj = JSON.parse(res);

	MakeMove(document.getElementById(obj.start),document.getElementById(obj.end));
	document.getElementById('move').style.background="green";

}


function MakeMove(a,b) {
  var pieceClass=a.className.split(' ')[1];

  b.innerText=a.innerText;
  b.className=b.className.split(' ')[0] + ' ' + pieceClass + ' moved';
  a.className = a.className.split(' ')[0] + ' moved';
  a.innerText='';
  a.style.background = "#a55"; b.style.background = "#a55"; 
  movecolor = invcolor(movecolor);
}