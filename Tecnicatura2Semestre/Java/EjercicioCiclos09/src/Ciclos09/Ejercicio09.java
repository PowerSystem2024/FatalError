
package Ciclos09;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio09 {

   
    public static void main(String[] args) {
       Scanner leer = new Scanner(System.in);
        // solicita los datos
                
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el dia"));
       
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Introduce el mes:"));
    
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Introduce el año:"));
        // Carga en la variable 'fechaValida' el resultado del metodo, que en este caso es true or false
           boolean fechaValida = validarFecha(dia, mes, anio);
       // evalua si la variable fechaValida es True la fecha sera correcta, caso contrario sera incorrecta
              
        if (fechaValida) {
             JOptionPane.showMessageDialog(null,"La fecha es correcta");
        } else {
            JOptionPane.showMessageDialog(null,"La fecha es incorrecta");
                    
        }
    }
    // METODO para validar la fecha
    public static boolean validarFecha(int dia, int mes, int anio) { //indico que el metodo devuelve un boolean e indico los parametros que recibe
        if (dia < 1 || dia > 30) {
            JOptionPane.showMessageDialog(null, "dia incorrecto");
           return false; // mes invalido
        }
        if (mes < 1 || mes > 12) {
            JOptionPane.showMessageDialog(null, "mes incorrecto");
           return false; // dia invalido
        }
        if (anio == 0) {
            JOptionPane.showMessageDialog(null, "anio incorrecto");
            return false; // anio invalido
        }
        JOptionPane.showMessageDialog(null, "la fecha ingresada es " + dia +"/"+ mes +"/"+ anio+ "/" );
        return true; // si pasa las validaciones, entonces el motodo devolvera true
    }
}
    


