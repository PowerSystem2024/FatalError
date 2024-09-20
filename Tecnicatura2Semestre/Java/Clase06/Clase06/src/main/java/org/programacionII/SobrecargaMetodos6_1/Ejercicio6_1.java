package org.programacionII.SobrecargaMetodos6_1;

public class Ejercicio6_1 {
    //Atributos  de esta clase
    public int a;
    public int b;
    //El constructor es un metodo especial
    //que sirve para instanciar objetos de esta clase
    public  Ejercicio6_1 () {
        System.out.println("ejecutando constructor uno");
    }
    //Estamos viendo lo que se llama sobrecarga de constructores
    public  Ejercicio6_1 (int a, int b) {
        this.a = a;
        this.b = b;
        System.out.println("ejecutando constructor dos");
    }
   //Metodo con Procedimiento sin retorno
    public void sumarNumeros(){
        int resultado = a+b;
        System.out.println(" resultado de sumar con metodo por procedimiento: "  + resultado);
    }
    //Metodo funcion con retorno
    public int sumarConReturn() {
        int resultado2 = a + b;
        return a + b;
       }
}
