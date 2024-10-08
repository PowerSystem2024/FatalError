// //let Persona3 = new Persona('Carla', 'Ponce'); esto no se debe hacer

class Persona { // Clase padre

    static contadorPersonas = 0; // Atributo estatico
    // email = "Valor default email"  // atributo NO estatico

    static get MAX_OBJ() { // este metodo simula una constante 
        return 5
    }

    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
        if (Persona.contadorPersonas < Persona.MAX_OBJ) {
            this.idPersona = ++Persona.contadorPersonas;
        }
        else {
            console.log("Se ha superado el max de objetos permitidos");
        }

        console.log("Se incrementa el contador: " + Persona.contadorPersonas);

    }

    get nombre() {
        return this._nombre;
    }

    set nombre(nombre) {
        this._nombre = nombre;
    }

    get apellido() {
        return this._apellido;
    }

    set apellido(apellido) {
        this._apellido = apellido;
    }

    static Saludar() {
        console.log("Saludos desde este método static");
    }

    static Saludar2(persona) {
        console.log(persona.nombre + ", " + persona.apellido);
    }


    nombreCompleto() {

        return this.idPersona + ' ' + this._nombre + ' ' + this._apellido;

    }

    toString() {
        return this.nombreCompleto();
    }
}

// Clase hija
class Empleado extends Persona {
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento() {
        return this._departamento;
    }

    set departamento(departamento) {
        this._departamento = departamento;
    }

    // Sobreescritura del método nombreCompleto()
    nombreCompleto() {
        return super.nombreCompleto() + ", " + this._departamento;
    }
}

// Ejemplos de uso
let persona1 = new Persona('Lilieth', 'Chacon');
console.log(persona1.nombre);  // Lilieth
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);  // Juan Carlos

let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);  // Carlos
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);  // Maria Laura

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1.toString());  // Maria Gimenez, Sistemas
console.log(empleado1.nombreCompleto());  // Maria Gimenez, Sistemas

// Método static
Persona.Saludar();  // Saludos desde este método static

Persona.Saludar2(persona1);
Empleado.Saludar();
Empleado.Saludar2(empleado1);


console.log(persona1.email);
console.log(empleado1.email);

console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());

//console.log(persona1.contadorPersonas);
console.log(Persona.contadorPersonas);

console.log(Empleado.contadorPersonas);

let Persona3 = new Persona("Carla", "Pertosi")

console.log(Persona3.toString());
console.log(Persona.contadorPersonas);

console.log(Persona.MAX_OBJ);
// Persona.MAX_OBJ = 10; No se puede modificar

let Persona4 = new Persona("Jorge", "Mathez")

console.log(Persona4.toString());

let Persona5 = new Persona("Morena", "Ruiz")

console.log(Persona5.toString());