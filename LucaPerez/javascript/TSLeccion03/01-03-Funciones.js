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

