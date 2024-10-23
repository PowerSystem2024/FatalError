package ciclos12;

import javax.swing.*;

/*  Pedir un numero y calcular su factorial, hacerlo con las dos clases Scanner y JOptionPane
 */
public class Ciclos12 {
    public static void main(String[] args) {
        long factorial = 1;
        //Scanner entrada = new Sacanner(Sytem.in);
        int numero = Integer.parseInt(JOptionPane.showInputDialog(("ingrese un numero: ")));
                for(int i = 1; i<=numero; i++){
                    factorial *= i;
                }
                //System.out.println("/n el factorial del numero ingreso es: "+ factorial) ;
        JOptionPane.showMessageDialog(null, "el factorial del número ingresado es: " + factorial);
    }
}
