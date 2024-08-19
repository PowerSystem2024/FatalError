// While
let contador = 0;
while(contador < 3){
    console.log(contador);
    contador++;
}
console.log("Fin del ciclo while");

//do while
let conteo = 0;
do{
    console.log(conteo);
    conteo++;
}while(conteo < 3);
console.log("Fin del ciclo do while");

//for
for(let contando = 0; contando < 3; contando++){
    console.log(contando);
}
console.log("Fin del ciclo for");

//Palabra reservada break
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando); //Muestra todos los pares
        break;
    }
}
console.log("Termina el ciclo al encontrar el primer numero par")   

//La palabra continue y Etiquetas Labels
inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        break inicio; // Continua y se dirige a la proxima iteracion   
    }
    console.log(contando);
}
console.log("Termina el ciclo");   

// Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
// Ejemplo de ejecucion: 0,3,6,9
console.log("Rango de 0 a 10 con numeros divisibles entre 3 son: ")
for(let i = 0; i < 11; i++){
    if(i % 3 != 0){
        continue;
    }
    console.log(i);
}

//Ejercicio 2: crear un rango de numeros de 2 a 6 e imprimirlos
//Ejemplo de ejecucion: 2,3,4,5,6
console.log("Rango de 2 a 6: ")
for(let i = 2; i < 7; i++){
    console.log(i)
}

//Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
// Ejemplo de ejecucion: 3,5,7,9
console.log("Rango de 3 a 10: ")
for(let i = 3; i < 11; i++){
    console.log(i);
}