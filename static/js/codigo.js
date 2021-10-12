// function modificar_caso(idcaso) {
//     xmlhttp = new XMLHttpRequest();
//     xmlhttp.open("GET", , true);
//     xmlhttp.send();
// }

function modificar_caso(idcaso) {
    $.ajax({
      type: 'POST',
      url: "/eliminar_caso",
      data: {idcaso: idcaso},
      dataType: "text",
      success: function(data){
                 alert("Se ah borrado el caso");
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