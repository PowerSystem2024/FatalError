// creacion de array o arreglos
//let autos = new Array('Ferrari', 'Lamborghini', 'Porsche', 'Audi', 'BMW'); // sintaxis antigua

const autos = ['Ferrari', 'Lamborghini', 'Porsche', 'Audi', 'BMW']; // sintaxis moderna
console.log(autos);

//recorremos los elementos de un arreglo
for (let i = 0; i < autos.length; i++) {
    console.log(autos[i]);
}

// modificamos un elemento de un arreglo
autos[1] = 'Maserati';
console.log(autos);

//agregamos nuevos elementos a un arreglo
autos.push('Mercedes Benz');
console.log(autos);

// otras formas de agregar elementos al arreglo
autos[autos.length] = 'Toyota';
console.log(autos);

// tercera forma de agregar elementos teniendo cuidado
autos[6] = 'Nissan';
console.log(autos); // se crea un espacio vacio en la posicion 5