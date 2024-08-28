
import javax.swing.JOptionPane;

public class Ejercicio01 {
    public static void main(String[] args) {
        int numero , cuadrado;
        
        numero =Integer.parseInt(JOptionPane.showInputDialog("Introduce un numero entero: ")); // abre una ventana para que el usuario ingrese la informacion
        while (numero >= 0) { //Mientras el numero ea igual a cero o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero" + numero + " elevado al cuadrado es: " + cuadrado);
            
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));// lee y ingresa el nuevo numero
        }
        System.out.println("Programa terminado por numero negativo");
    }
}
