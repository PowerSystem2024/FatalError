let x = 10; //primitiva
console.log(x.length); undefined
console.log("Tipos primitivos");
//creamos objeto 
let persona = {
    nombre: "Morena",
    apellido: "Ruiz",
    email: "morenaruiz@gmail.com",
    edad: 222,
    idioma: "ES",
    get lang(){
        console.log (this.idioma.toUpperCase());
    },
    set lang(lang){
        console.log(this.idioma = lang.toUpperCase());
    },
    nombreCompleto: function(){ //metodo
        return this.nombre+" "+this.apellido;
    },
    get nombreEdad(){
        return "El nombre es: "+this.nombre+", Edad : "+this.edad;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log("Ejecutando con un objeto");
let persona2 = new Object(); //crear nuevo objeto
persona2.nombre = "Zoe";
persona2.direccion = "Nose 123";
persona2.telefono = "123321123";
console.log(persona2.telefono);
console.log("Creamos un nuevo objeto");
console.log(persona["apellido"]); //como si fuera un arreglo
console.log("Usamos el ciclo for in");

//for in
for(propiedad in persona){
    console.log(propiedad); 
    console.log(persona[propiedad]);
}
console.log("Cambiamos y eliminamos un error");
persona.apellida = "Carrizo"; //cambiamos dinamicamente
delete persona.apellida; //eliminamos error
console.log(persona);

//Diferentes formas de imprimir un objeto
console.log("Diferentes formas de imprimir un objeto");
//Forma 1: concatenando 
console.log("Forma una: concatenando");
console.log(persona.nombre+", "+persona.apellido);

//Forma 2: ciclo for in
console.log("Forma dos: ciclo for in");
for(nombrePropiedad in persona){
   console.log(persona[nombrePropiedad]);
}

//Forma 3: funcion Object.values()
console.log("Forma tres: funcion Object.values()")
let personaArray = Object.values(persona);
console.log(personaArray);

//Forma 4: metodo JSON.stringify
console.log("Forma cuatro: metodo JSON.stringify");
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log("Comenzamos a utilizar el metodo get");
console.log(persona.nombreEdad);

console.log("Comenzamos con el metodo get y set para idiomas");
persona.lang = "en";
console.log(persona.lang);

function Persona3(nombre = "Juan", apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+" "+this.apellido;
    }
}
let padre = new Persona3("Agustin", "Ruiz", "agusruiz@gmail.com");
padre.nombre = "Carlos";
console.log(padre);
console.log(padre.nombreCompleto());
let madre = new Persona3("Paola", "Carrizo", "paocarrizo@gmail.com");
console.log(madre);
console.log(madre.nombreCompleto());