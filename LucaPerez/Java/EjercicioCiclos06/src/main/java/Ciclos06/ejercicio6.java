/*
Ejercicio 6: Pedir numeros hasta que se teclee un o , mostrar
la suma de todos los numeros introducidos.

con JOptionPane
*/
package Ciclos06;

import javax.swing.JOptionPane;

public class ejercicio6 {
    public static void main(String[] args) {
        int numero , suma = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog(suma));
            suma+= numero;
        }while(numero!=0);
        JOptionPane.showMessageDialog(null, "\n La suma de todos los numeros ingresados es:"+ suma);
        
        
    }
    
}
