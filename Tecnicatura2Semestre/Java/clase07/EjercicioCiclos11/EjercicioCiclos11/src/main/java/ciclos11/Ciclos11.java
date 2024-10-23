package ciclos11;

import javax.swing.*;
/* consigna11: diseñar un programa que muestre el producto
de los 10 primero numeros impares hacerlo con JOptionPane
 */


public class Ciclos11 {
    public static void main(String[] args) {
        long producto =1;
        for(int i = 1; i<=20; i+=2){
            producto *=  i;
        }
        JOptionPane.showMessageDialog(null, "el producto de los numeros impares es: " + producto );
    }
}
