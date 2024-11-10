/*
Ejercicio 2: Leer un numero e indicar si es negativo o positivo
Este proceso se repetira hasta que se introduzca un 0
Hacer este ejercicio con la clase Scanner
Luego hacer este ejercicio con la clase JOptionPane
*/
package Ciclos02;

import javax.swing.JOptionPane;


public class Ciclos02 {
    public static void main(String[] args) {
        System.out.println("Digite un numero: ");
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero != 0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es POSITIVO");
            }
            else{
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero "+numero+" finaliza el programa");
    }
}
