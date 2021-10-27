// function modificar_caso(idcaso) {
//     xmlhttp = new XMLHttpRequest();
//     xmlhttp.open("GET", , true);
//     xmlhttp.send();
// }

function borrar_caso(idcaso, userid) {
	$.ajax({
		type: 'DELETE',
		url: "/eliminar_caso",
		data: { idcaso: idcaso },
		dataType: "text",
		success: function () {
			window.location.href = "/casos/" + userid;
		}
	});
};

function comentar(idcaso, userid) {
	var comentario = document.getElementById("coment");
	var foto = "";
	foto = document.getElementById("foto");
	$.ajax({
		type: 'POST',
		url: "/comentar",
		data: {
			userid: userid,
			comentario: comentario,
			idcaso: idcaso,
			foto: foto
		},
		dataType: "text",
		success: function () {
			window.location.href = "/vercaso/" + idcaso;
		}
	});
};

function load() {
	var file = document.getElementById('foto').files[0]

	var reader = new FileReader()

	reader.readAsDataURL(file);
	reader.onload = function () {
		var imgUrlBase64 = this.result
		document.getElementById('show').value = imgUrlBase64
	}
}

let boton = document.getElementById("boton1");
if (boton) {
	boton.addEventListener("click", function (e) {
		e.preventDefault();
		var img = document.getElementById("imagen-caso");
		img.style.display = "block";
		boton.classList.toggle("alternador");
		boton.classList.toggle("display-none");
	})
}



function validateProfileDHTML(form) {
	var retorno = true;
	var errores = "";

	form["clave"].className = ""
	form["confirm"].className = ""
	form["vieja"].className = ""

	if (form["clave"].value.trim() == "") {
		errores += "<li><b>clave</b> is required"
		form["clave"].className = "inputError"
		if (retorno) form["clave"].focus()
		retorno = false;
	}

	if (form["confirm"].value.trim() == "") {
		errores += "<li><b>confirm</b> is required"
		form["confirm"].className = "inputError"
		if (retorno) form["confirm"].focus()
		retorno = false;
	}

	if (form["vieja"].value.trim() == "") {
		errores += "<li><b>vieja</b> is required"
		form["vieja"].className = "inputError"
		if (retorno) form["vieja"].focus()
		retorno = false;
	}

	if (form["clave"].value != form["confirm"].value) {
		errores += "<li><b>La clave nueva</b> no coincide"
		form["clave"].className = "inputError"
		form["confirm"].className = "inputError"
		if (retorno) form["confirm"].focus()
		retorno = false;
	}

	if (!retorno) {
		document.getElementById("errores_profile").innerHTML = errores
		document.getElementById("errores_profile").style.display = "block"
		document.getElementById("error").style.display = "none"
	}

	return (retorno);
}

function validarlogin(form) {
	var retorno = true;
	var errores = "";

	form["email"].className = ""
	form["clave"].className = ""

	if (form["email"].value.trim() == "") {
		errores += "<li><b>El correo</b> es requerido"
		form["email"].className = "inputError"
		if (retorno) form["email"].focus()
		retorno = false;
	}

	if (form["clave"].value.trim() == "") {
		errores += "<li><b>La clave</b> es requerida"
		form["clave"].className = "inputError"
		if (retorno) form["clave"].focus()
		retorno = false;
	}

	if (!retorno) {
		document.getElementById("errores_profile").innerHTML = errores
		document.getElementById("errores_profile").style.display = "block"
		document.getElementById("error").style.display = "none"
	}

	return (retorno);
}

function validarsignup(form) {
	var retorno = true;
	var errores = "";

	form["nombre"].className = ""
	form["usuario"].className = ""
	form["email"].className = ""
	form["clave"].className = ""
	form["confirm"].className = ""

	if (form["nombre"].value.trim() == "") {
		errores += "<li><b>El nombre</b> es requerido"
		form["nombre"].className = "inputError"
		if (retorno) form["nombre"].focus()
		retorno = false;
	}
	if (form["usuario"].value.trim() == "") {
		errores += "<li><b>El usuario</b> es requerido"
		form["usuario"].className = "inputError"
		if (retorno) form["usuario"].focus()
		retorno = false;
	}
	if (form["email"].value.trim() == "") {
		errores += "<li><b>El correo</b> es requerido"
		form["email"].className = "inputError"
		if (retorno) form["email"].focus()
		retorno = false;
	}
	if (form["clave"].value.trim() == "") {
		errores += "<li><b>La clave</b> es requerida"
		form["clave"].className = "inputError"
		if (retorno) form["clave"].focus()
		retorno = false;
	}
	if (form["confirm"].value.trim() == "") {
		errores += "<li><b>El confirmacion</b> es requerido"
		form["confirm"].className = "inputError"
		if (retorno) form["confirm"].focus()
		retorno = false;
	}


	if (form["clave"].value != form["confirm"].value) {
		errores += "<li><b>Las claves</b> no coinciden"
		form["clave"].className = "inputError"
		form["confirm"].className = "inputError"
		if (retorno) form["confirm"].focus()
		retorno = false;
	}
	if (!retorno) {
		document.getElementById("errores_profile").innerHTML = errores
		document.getElementById("errores_profile").style.display = "block"
		document.getElementById("error").style.display = "none"
	}

	return (retorno);
}

let cerrar = document.querySelectorAll(".close")[0];
let abrir = document.querySelectorAll(".cta")[0];
let modal = document.querySelectorAll(".modal")[0];
let modalC = document.querySelectorAll(".modal-container")[0];

if (abrir) {
	abrir.addEventListener("click", function (e) {
		e.preventDefault();
		modalC.style.opacity = "1";
		modalC.style.visibility = "visible";
		modal.className = "modal";
	})
}
if (cerrar) {
	cerrar.addEventListener("click", function (e) {
		e.preventDefault();
		modal.className = "modal modal-close";
		setTimeout(function () {
			modalC.style.opacity = "0";
			modalC.style.visibility = "hidden";
		}, 850);
	})
}
window.addEventListener("click", function (e) {
	if (e.target == modalC) {
		modal.className = "modal modal-close";
		setTimeout(function () {
			modalC.style.opacity = "0";
			modalC.style.visibility = "hidden";
		}, 850);
	}
	if (e.target == modalCR) {
		modalR.className = "modal modal-close";
		setTimeout(function () {
			modalCR.style.opacity = "0";
			modalCR.style.visibility = "hidden";
		}, 850);
	}
	if (e.target == modalCC) {
		modalComent.className = "modal modal-close";
		setTimeout(function () {
			modalCC.style.opacity = "0";
			modalCC.style.visibility = "hidden";
		}, 850);
	}
})

let cerrarR = document.getElementById("close");
let abrirR = document.getElementById("finalizar");
let modalR = document.getElementById("mfinal");
let modalCR = document.getElementById("mcontainer");

if (abrirR) {
	abrirR.addEventListener("click", function (e) {
		e.preventDefault();
		modalCR.style.opacity = "1";
		modalCR.style.visibility = "visible";
		modalR.className = "modal";
	})
}

if (cerrarR) {
	cerrarR.addEventListener("click", function (e) {
		e.preventDefault();
		modalR.className = "modal modal-close";
		setTimeout(function () {
			modalCR.style.opacity = "0";
			modalCR.style.visibility = "hidden";
		}, 850);
	})
}

function cambiar_edit(id){
	var modalP = document.getElementById(id);
	var modalE = document.getElementById(id + "edit");
	modalP.style.display = "none";
	modalE.style.display = "block";
}

function cambiar_coment(id){
	var modalP = document.getElementById(id);
	var modalE = document.getElementById(id + "edit");
	modalP.style.display = "block";
	modalE.style.display = "none";
}

function editar_comentario(id, idcaso){
	var comentario = document.getElementById("coment_edit");
	var foto = document.getElementById("foto_edit");
	$.ajax({
		type: 'POST',
		url: "/editar_coment",
		data: { idcoment: id,
				comentario: comentario.value,
				foto: foto.value},
		success: function () {
			window.location.href = "/vercaso/" + idcaso;
		}
	});
}

let cerrarC = document.getElementById("closeC");
let borrarC;
let modalComent = document.getElementById("coment_m");
let modalCC = document.getElementById("coment_modal");

function abrir_comentario(idcomentario) {
	borrarC = idcomentario;
	modalCC.style.opacity = "1";
	modalCC.style.visibility = "visible";
	modalComent.className = "modal";

}

function borrar_comentario(idcaso) {
	$.ajax({
		type: 'DELETE',
		url: "/eliminar_coment",
		data: { idcomentario: borrarC },
		success: function () {
			window.location.href = "/vercaso/" + idcaso;
		}
	});
};


if (cerrarC) {
	cerrarC.addEventListener("click", function (e) {
		e.preventDefault();
		modalComent.className = "modal modal-close";
		setTimeout(function () {
			modalCC.style.opacity = "0";
			modalCC.style.visibility = "hidden";
		}, 850);
	})
}

$(function () {
	$("input[required]").parent().prev().append($("<span>").text("*").addClass("required"));
	$("select[required]").parent().prev().append($("<span>").text("*").addClass("required"));
})

$(document).ready(function () {

	var now = new Date();

	var day = ("0" + now.getDate()).slice(-2);
	var month = ("0" + (now.getMonth() + 1)).slice(-2);

	var hours = now.getHours();
	var minutes = now.getMinutes();
	var seconds = now.getSeconds();
	var today = now.getFullYear() + "-" + (month) + "-" + (day) + "T" + (hours) + ":" + (minutes) + ":" + (seconds);
	$("#date").val(today);
	fecha = today;
});

let fecha;
function finalizar_caso(idcaso) {
	$.ajax({
		type: 'PUT',
		url: "/casos/finalizar",
		data: {
			idcaso: idcaso,
			date: fecha
		},
		dataType: "text",
		success: function () {
			window.location.href = "/vercaso/" + idcaso;
		}
	});
};