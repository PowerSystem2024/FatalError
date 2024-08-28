/*
Ejercicio 5 : Realizar un juego para adivinar un numero,
para ello generar un numero aleatorio entre o-100 y
luego ir pidiendo numeros indicando "Es mayor" o
"Es menor" segun sea mayor o menor con respecto a N
El proceso termina cuando el usuario acierta y mostramos
el numero de intentos hechos
*/


package Ciclos05;

import java.util.Scanner;


public class Ciclos05 {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio , conteo = 0;
        aleatorio = (int)(Math.random()*100); // esto genera un numero aleatorio
        do{
            System.out.println("Digite un numero");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero< aleatorio){
                System.out.println("Digite un numero mayor");
            }
            else if(numero > aleatorio){
                System.out.println("Digite un numero menor");
            }
            else{
                System.out.println("FELICIDADES!!! HAS ADIVINADO EL NUMERO");
            }
            conteo++;
        }while(numero != aleatorio);
        System.out.println("adivinaste el numero en:" + conteo + "Intentos");
           
        
    }
    
}
