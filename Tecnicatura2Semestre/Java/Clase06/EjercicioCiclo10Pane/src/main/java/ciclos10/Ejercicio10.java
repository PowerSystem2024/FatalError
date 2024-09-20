package ciclos10;

import javax.swing.*;
import java.util.Scanner;

public class Ejercicio10 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int numero, suma = 0;
        for (int i = 1; i <= 10; i++) {
             numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero en la posicion "+ i + ":"));
            suma += numero;
        }
        JOptionPane.showMessageDialog(null, "la suma de todos los numeros ingresados es: " + suma);
    }
}


