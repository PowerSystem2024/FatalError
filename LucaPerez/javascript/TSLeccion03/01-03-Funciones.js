miFuncion(8,2); //esto se le conoce como hosting

function    miFuncion(a,b){
    //console.log("Sumamos: " + (a+b));
    return a+b;
}

//llamada a la función
miFuncion(5,4);
console.log(miFuncion(5,4));

let resultado = miFuncion(6,7);
console.log(resultado);

//declaramos otra funcion de tipo expresion o anonima
let x = function(a,b){return a+b}; // nesecita cierre con punto y coma
resultado = x(5,6); // al llamarla se pone la variable y parentesis
console.log(resultado);

//funciones de tipo self y invoking (no se puede reutilizar)
(function(a,b){
    console.log("Ejecutando la funcion: " + (a+b));
})(9,6);

console.log(typeof miFuncion);
function    miFuncionDos(a,b){
    console.log(arguments.length);
}

miFuncionDos(10,2,3,4,5,6);

//toString
var miFuncionTexto = miFuncion.toString(); //  metodo toString: convierte a texto asignamos nuestra funcion pero en forma de texto
console.log(miFuncionTexto);

//funciones flecha
const sumarFuncionTipoFlecha = (a,b) => a+b; // se quita la palabra function y se ponen flechas
resultado = sumarFuncionTipoFlecha(3,7);
console.log(resultado);


//funcion de tipo expresion
let sumar = function(a =4,b =8){ // se le asigna un valor por defecto
    console.log(arguments[0]) ; // muestra el parametro de : a
    console.log(arguments[1]) ; // muestra el parametro de : b
    return a+b + arguments[2]; // se le asigna un valor por defecto{3}
}

resultado = sumar(3,2,9);
console.log(resultado);


let respuesta = sumarTodo(5,4,13,10,9);
console.log(respuesta);

// a esto se le llama hosting
//sumar todos los argumentos
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i]; // arguments es para arreglos
    }
    return suma;
}


// tipos primitivos
let k = 10;
function cambiarValor(a){ // paso por valor (la variable no sufre ningun cambio)
    a = 20;
}

cambiarValor(k);
console.log(k);


// paso por referencia
const persona = {
    nombre: "Juan",
    apellido: "Perez"
}
console.log(persona);

function cambiarValorObjeto(p1){
    p1.nombre = "Carlos";
    p1.apellido = "Lara";
}

cambiarValorObjeto(persona);
console.log(persona);
