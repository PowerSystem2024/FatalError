/*
 
Ejercicio 4 : Pedir numeros hasta que se teclee uno negativo,
y mostrar cuanto numeros se han introducido.
lo hacemos primero con la clase Scanner
Luego lo hacemos con la clase JOptionPane

 */
package Ciclos04;

import java.util.Scanner;


public class Ciclos04 {
    public static void main(String[] args){
        Scanner entrada = new Scanner (System.in);
        int numero , conteo = 0;
        System.out.println("Digite un numero:");
        
        numero = Integer.parseInt(entrada.nextLine());
        while(numero>= 0){
            System.out.println("el numero "+ numero + " Es positivo");
            conteo++;
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(entrada.nextLine());
        }
        
        System.out.println("A ingresado " + conteo + " numero que no son negativos");
        
        
    }
    
}
