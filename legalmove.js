getTxt = function (){

  $.ajax({
    url:'data/text.txt',
    success: function (data){
    	console.log(data);
      //parse your data here
      //you can split into lines using data.split('\n') 
      //an use regex functions to effectively parse it
    }
  });
}

function loadDoc() {

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
  	console.log(this.readyState, this.status)
    if (this.readyState == 4 && this.status == 200) {
    	console.log(1)
    	console.log(this.responseText)
      document.getElementById("demo").innerHTML =
      this.responseText;
    }
  };
  xhttp.open("GET", "data/text.txt", true);
  xhttp.send();
}

function IfLegalMove(e) {
	var x = event.clientX, y = event.clientY,
	cell = document.elementFromPoint(x, y);
	if(!isCell(cell)) return 0;
return 1;
}
