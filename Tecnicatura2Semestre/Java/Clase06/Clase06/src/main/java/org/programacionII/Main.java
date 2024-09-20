package org.programacionII;

import org.programacionII.SobrecargaMetodos6_1.Ejercicio6_1;

import java.util.MissingFormatArgumentException;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        miMetodo();

        Ejercicio6_1 aritmetica1 = new Ejercicio6_1();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();

        int resultado = aritmetica1.sumarConReturn();
        System.out.println("resultado con retorno es : " + resultado);

        System.out.println("aritmetica1 a: " + aritmetica1.a);
        System.out.println("aritmetica1 b: " + aritmetica1.b);

        Ejercicio6_1 aritmetica2 = new Ejercicio6_1(5, 8);

        System.out.println("aritmetica2 a = " + aritmetica2.a);
        System.out.println("aritmetica2 b = " + aritmetica2.b);
    }
//DEMOSTRACION DEL ALCANCE DE UNA VARIABLE CORRESPONDIENTE AL VIDEO 6.2 DE LA CLASE 6
        public static void miMetodo(){
           // int a = 100;
            System.out.println("miMetodo se esta ejecuntando demostrando que el alcance de una variable es inferior al alcance de un atributo de Clase");
        }
}