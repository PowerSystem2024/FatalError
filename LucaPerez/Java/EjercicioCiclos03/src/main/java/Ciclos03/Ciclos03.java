/*
Ejercicio 3 : leer numeros hasta que se introduzca un cero
para cada uno indica si es par o impar.
primero lo haremos con la clase Scanner
Luego con la clase JOptionPane
*/
package Ciclos03;

import java.util.Scanner;

public class Ciclos03 {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        
        while(numero != 0){
            if (numero % 2 == 0) {
                System.out.println("el numero ingresado   " + numero + "Es par" );
            }
            else{
                System.out.println("El numero ingresado " + numero + "Es impar");
            }
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("EL numero  ingresado es " + numero + "finaliza el proceso");
    }
    
}
