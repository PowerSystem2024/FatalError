/*
ejercicio 1: Leer un numero y mostrar su cuadrado , repetir el proceso hasta 
que se introduzca un numero negativo
 */


import java.util.Scanner;

public class Ciclos01{
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int numero , cuadrado;
        System.out.println("Introduce un numero entero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero >= 0) { //Mientras el numero ea igual a cero o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero" + numero + " elevado al cuadrado es: " + cuadrado);
            System.out.println("Introduce un otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());// lee y ingresa el nuevo numero
        }
        System.out.println("Programa terminado por numero negativo");

    }

}