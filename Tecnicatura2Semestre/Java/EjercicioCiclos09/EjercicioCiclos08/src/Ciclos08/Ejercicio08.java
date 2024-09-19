
package Ciclos08;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio08 {

    public static void main(String[] args) {        
       
        int numero = Integer.parseInt(JOptionPane.showInputDialog("ingrese un numero"));
        int i = 1;
        
        while(i <=numero){
            JOptionPane.showMessageDialog(null,i);
              i++;
           }
        
        
    }

}
