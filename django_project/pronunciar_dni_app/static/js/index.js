function ProcesarDni () {
    var dni = document.getElementById("dni_input").value;
    if (dni.length > 0) {
        location.href = '/result/'+dni;
    }
    else {
        alert("Ingresa un dni valido!");
    }
}