//while
let contador = 0;
while(contador<3){
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

//para reservaa break
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando);//muestra todos los pares
        break; 
    }
    
}
console.log("Fin del ciclo for al encontrar el primer numero par");

//palabra reservada continue y Etiquetas Labels
inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        break inicio; // ir a la siguiente iteracion
    }
    console.log(contando);
}

console.log("Fin del ciclo for al encontrar el primer numero par");
