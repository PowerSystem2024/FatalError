package Ciclos09;
import java.util.Scanner;
/*
Ingresar dia mes y anio, de una fecha, indicar si la fecha es correcta. Suponiendo que los meses son de 30 dias
*/
public class Ciclos09 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // solicita los datos
        System.out.println("Introduce el día:");
        int dia = sc.nextInt();
       System.out.println("Introduce el mes:");
        int mes = sc.nextInt();
        System.out.println("Introduce el anio:");
        int anio = sc.nextInt();
        // Carga en la variable 'fechaValida' el resultado del metodo, que en este caso es true or false
           boolean fechaValida = validarFecha(dia, mes, anio);
       // evalua si la variable fechaValida es True la fecha sera correcta, caso contrario sera incorrecta
        if (fechaValida) {
            System.out.println("La fecha es correcta.");
        } else {
            System.out.println("La fecha es incorrecta.");
        }
    }
    // METODO para validar la fecha
    public static boolean validarFecha(int dia, int mes, int anio) { //indico que el metodo devuelve un boolean e indico los parametros que recibe
        if (dia < 1 || dia > 30) {
           return false; // mes invalido
        }
        if (mes < 1 || mes > 12) {
           return false; // dia invalido
        }
        if (anio == 0) {
            return false; // anio invalido
        }
        return true; // si pasa las validaciones, entonces el motodo devolvera true
    }
}
    


