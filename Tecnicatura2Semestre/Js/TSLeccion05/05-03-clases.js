//let Persona3 = new Persona('Carla', 'Ponce'); esto no se debe hacer

class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;

    }

    set apellido(apellido){
        this._apellido = apellido;
    }
}

let persona1 = new Persona('Lilieth', 'Chacon');
console.log(persona1.nombre);
persona1.nombre = 'juan carlos';
console.log(persona1.nombre);


//console.log(persona1);

let persona2 = new Persona('Carlos', 'Lara');
//console.log(persona2);
console.log(persona2.nombre);
persona2.nombre = 'Maria laura';
console.log(persona2.nombre);

