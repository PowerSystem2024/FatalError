let x = 10; //primitiva
console.log(x.length); undefined
console.log("Tipos primitivos");
//creamos objeto 
let persona = {
    nombre: "Morena",
    apellido: "Ruiz",
    email: "morenaruiz@gmail.com",
    edad: 22,
    nombreCompleto: function(){ //metodo
        return this.nombre+" "+this.apellido;
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
