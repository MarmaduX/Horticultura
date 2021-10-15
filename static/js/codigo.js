// function modificar_caso(idcaso) {
//     xmlhttp = new XMLHttpRequest();
//     xmlhttp.open("GET", , true);
//     xmlhttp.send();
// }

function borrar_caso(idcaso, userid) {
    $.ajax({
      type: 'DELETE',
      url: "/eliminar_caso",
      data: {idcaso: idcaso},
      dataType: "text",
      success: function(data){
                 alert("Se ah borrado el caso");
                 window.location.href  = "/casos/"+userid;
               }
    });
};

function load() {
  var file = document.getElementById('foto').files[0]
  
  var reader = new FileReader()

  reader.readAsDataURL(file);
  reader.onload = function() {
    var imgUrlBase64 = this.result
    document.getElementById('show').value = imgUrlBase64
  }
}


function setImageDisplay(id) {
  var img = document.getElementById(id);
  img.style.display = "block";  
}

function validateProfileDHTML(form) {
	var retorno = true;
	var errores = "";

	form["clave"].className = ""
	form["confirm"].className = ""
	form["vieja"].className = ""

	if(form["clave"].value.trim() == "") {
		errores += "<li><b>clave</b> is required"
		form["clave"].className = "inputError"
		if(retorno) form["clave"].focus()
		retorno = false;
	}

	if(form["confirm"].value.trim() == "") {
		errores += "<li><b>confirm</b> is required"
		form["confirm"].className = "inputError"
		if(retorno) form["confirm"].focus()
		retorno = false;
	}

	if(form["vieja"].value.trim() == "") {
		errores += "<li><b>vieja</b> is required"
		form["vieja"].className = "inputError"
		if(retorno) form["vieja"].focus()
		retorno = false;
	}

	if(form["clave"].value != form["confirm"].value) {
		errores += "<li><b>La clave nueva</b> no coincide"
		form["clave"].className = "inputError"
		form["confirm"].className = "inputError"
		if(retorno) form["confirm"].focus()
		retorno = false;
	}

	if(! retorno) {
	    document.getElementById("errores_profile").innerHTML = errores
	    document.getElementById("errores_profile").style.display = "block"
      document.getElementById("error").style.display = "none"
	}

	return(retorno);
}