/*
Ejercicio 6: Pedir numeros hasta que se teclee un o , mostrar
la suma de todos los numeros introducidos.
*/
package Ciclos06;

import java.util.Scanner;

public class ciclos06 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero , suma = 0;
        do{
            System.out.println("Digite un numero");
            numero = Integer.parseInt(entrada.nextLine());
            suma+= numero;
        }while(numero!=0);
        System.out.println("\n La suma de todos los numeros ingresados es:"+ suma);
        
    }
    
}
