/*
Ejercicio 3: Crear y cargar una matriz de tamaño 3x3, transportarla y mostrarla.
*/
package matriz_ejercicio_3;

import java.util.Scanner;

public class Matriz_Ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz [][] = new int [3][3];
        
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.println("Matriz ["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        System.out.println();
        
        System.out.println("\nMatriz original: ");
        for (int i = 0; i < 3; i++) {
                 for (int j = 0; j < 3; j++) {
                          System.out.println(matriz[i][j]+"  ");
                 }
                 System.out.println();
        }
        System.out.println();
        
        //Matriz transpuesta
        System.out.println("\nMatriz Transpuesta: ");
        for (int i = 0; i < 3; i++) {
                 for (int j = 0; j < 3; j++) {
                          System.out.println(matriz[i][j]+"  ");
                 }
                 System.out.println();
        }
        System.out.println();
    }
}
