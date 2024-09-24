//let Persona3 = new Persona('Carla', 'Ponce'); esto no se debe hacer

class Persona { //clase padre
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

class Empleado extends Persona{ //clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;

    }
    set departamento(departamento){
        this._departamento = departamento;
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


let Empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(Empleado1);
console.log(Empleado1.nombre);


