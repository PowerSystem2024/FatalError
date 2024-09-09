/*Hosting, propiedad que permite llamar a la funcion antes
o despues de ser declarada
*/
miFuncion(8,2)

//Colocamos funcion + nombre + parametros
function miFuncion(a,b){
    //console.log("Sumamos: "+(a+b));
    return a+b;
}

//Llamamos a la funcion colocando los argumentos 
miFuncion(5,4);

let resultado = miFuncion(6,7);
console.log(resultado)

console.log("DECLARAMOS UNA FUNCION DE TIPO EXPRESION o ANONIMA")
//DECLARAMOS UNA FUNCION DE TIPO EXPRESION o ANONIMA
let x = function(a,b){return a + b};//necesita cierre
resultado = x(5,6);
console.log(resultado)

//FUNCIONES DE TIPO SELF E INVOKING
//(function(a,b){
//    console.log("Ejecutando la funcion: " +(a+b));
//})(9,6);

console.log("A que tipo pertenece un funcion")
console.log(typeof miFuncion);
function miFuncion2(a,b){
    console.log(arguments)
}
miFuncion2(5,7)

console.log("toString")
//toString 
var miFuncionTexto = miFuncion2.toString();
console.log(miFuncionTexto)

console.log("Funciones Flecha")

//Funciones flecha
const sumarFuncionFlecha = (a,b) => a+b;
resultado = sumarFuncionFlecha(3,7);
console.log(resultado);

/*PARAMETROS Y ARGUMENTOS
CUANDO DEFINIMOS UNA FUNCION, LOS DATOS QUE RECIBE SE LLAMA PARAMETROS
cuando LLAMAMOS a una funcion los datos que recibe son ARGUMENTOS
*/

let sumar = function(a=4,b=8){
    console.log(arguments[0]);//Muestra el parametro de a y no de b
    console.log(arguments[1]);//muestra el parametro de b
    return a + b + arguments[2];
}
resultado = sumar(3,2.9);
console.log(resultado);

//HOSTING
//sumar todos los argumentos
let respuesta = sumarTodo(5,4,13,10,9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i];
    }
    return suma;
}
//TIPOS PRIMITIVOS - PASO POR VALOR 
let k = 10;
function cambiarValor(a){
    a = 20; //K va a valer 20 acá
}
cambiarValor(k);
console.log(k); //K acá ya vuelve a valer 10

//TIPOS PRIMITIVOS PASO POR REFERENCIA

const persona = {
    nombre: "Juan",
    apellido: "Lepez"
} 
console.log(persona);

function cambiarValorObjeto(p1){
    p1.nombre = "Ignacio";
    p1.apellido = "Perez";
}
cambiarValorObjeto(persona);
console.log(persona);