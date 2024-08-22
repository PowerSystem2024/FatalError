package leccion02;

import java.util.Scanner;

public class ejercicioCiclos02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Introduce un numero entero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0) {
            if (numero >0) {
                System.out.println("El numero " + numero + " es positivo " );
            }
            else{
                System.out.println("El numero " + numero + " es negativo " );
            }
            System.out.println("Introduce otro numero: ");
            numero = Integer.parseInt((entrada.nextLine()));
        
        }
        System.out.println("El numero" + numero + " Finaliza el programa");
    }
}
