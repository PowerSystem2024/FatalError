/*
Ejercicio 3 : leer numeros hasta que se introduzca un cero
para cada uno indica si es par o impar.
primero lo haremos con la clase Scanner
Luego con la clase JOptionPane
*/
package Ciclos03;

import javax.swing.JOptionPane;


public class Ejercicio03 {
    public static void main(String[] args) {
    int numero;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while(numero != 0){
            if (numero % 2 == 0) {
                JOptionPane.showMessageDialog(null, "el numero ingresado   " + numero + "Es par" );
            }
            else{
                JOptionPane.showMessageDialog(null, "el numero ingresado   " + numero + "Es inpar" );
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
            
        }
        JOptionPane.showMessageDialog(null,"El numero ingresado es " + numero + "Finaliza el programa");
    }
    
    
    }
     
   
