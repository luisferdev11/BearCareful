function validar(event){

    var correo = document.getElementById("inputCorreo").value;
    var contraseña = document.getElementById("inputContraseña").value;

    var validacion1 = validacionCaracteresEspeciales(correo + contraseña);
    var validacion2 = validacionTamaño(correo, contraseña);
    var validacion3 = validacionEspacios(correo, contraseña);
    var validacion4 = validacionTextoVacio(correo, contraseña);

    if(validacion1 == false | validacion2 == false | validacion3 == false | validacion4 == false){
        event.preventDefault();
    }

}

function validacionCaracteresEspeciales(input){
    if(/"|'|,|<|>/.test(input)==true){
        alert("No puedes usar comilla simple, comillas, comas o los simbolos mayor y menor que.");
        return false;
    }
}

function validacionTamaño(input1, input2){
    if(input1.length < 8 | input2.length < 3){
        alert("Debes usar minimo 8 caracteres.");
        return false;
    }
}

function validacionEspacios(input1, input2){
    if(/ /g.test(input1)==true | / /g.test(input2)==true){
        alert("No puedes usar espacios.")
        return false;
    }
}

function validacionTextoVacio(input1, input2){
    if(input1.replace(/ /g,"")=="" | input2.replace(/ /g,"")==""){
        alert("No puedes dejar campos vacios.")
        return false;
    }
}