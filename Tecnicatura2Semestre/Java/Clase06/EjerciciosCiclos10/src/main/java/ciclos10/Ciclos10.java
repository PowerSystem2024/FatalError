package ciclos10;
import java.util.Scanner;
public class Ciclos10 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int numero, suma = 0;
        for (int i = 1; i <= 10; i++) {
            System.out.println("ingrese un numero en la posicion " + i + ":");
            numero = Integer.parseInt(leer.nextLine());
            suma += numero;
        }
        System.out.println("La suma de todos los numeros es: " + suma);
    }
}