/*
Ejercicio 5 : Realizar un juego para adivinar un numero,
para ello generar un numero aleatorio entre o-100 y
luego ir pidiendo numeros indicando "Es mayor" o
"Es menor" segun sea mayor o menor con respecto a N
El proceso termina cuando el usuario acierta y mostramos
el numero de intentos hechos
*/


package Ciclos05;

import javax.swing.JOptionPane;


public class Ejercicio05 {
    public static void main(String[] args) {
        int numero, aleatorio , conteo = 0;
        aleatorio = (int)(Math.random()*100); // esto genera un numero aleatorio
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero:" ));
            if(numero< aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un numero mayor");
            }
            else if(numero > aleatorio){
               JOptionPane.showMessageDialog(null,"Digite un numero menor");
            }
            else{
                JOptionPane.showMessageDialog(null, "FELICIDADES!!! HAS ADIVINADO EL NUMERO");
            }
            conteo++;
        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null, "adivinaste el numero en:" + conteo + "Intentos");
    
    }
}
