//var result_cat = encodeURIComponent(sel_cat);


function postAction(a,d){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "postAction.py", true)
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
    xhr.send("action=" + a + "&" + d);
    xhr.onreadystatechange = function (){ 
		if(xhr.readyState == 4){ 
			alert(xhr.responseText);
		} 
	} 
}
