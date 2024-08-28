
package Ciclos04;

import javax.swing.JOptionPane;


public class Ejercicio04 {
     public static void main(String[] args){
        int numero , conteo = 0;
        System.out.println("Digite un numero:");
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while(numero>= 0){
            JOptionPane.showMessageDialog(null, "el numero "+ numero + " Es positivo");
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
          
        }
        JOptionPane.showMessageDialog(null, "A ingresado " + conteo + " numero que no son negativos");
      
    }
    
}
