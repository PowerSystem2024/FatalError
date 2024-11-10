/*
Proyecto caja:
Ejercicio 1: Crear un proyecto segun las especificaciones mostradas
a continuacion: 
La formula es: Volumen = ancho * alto * profundidad
*/
package caja;

public class Caja { //Clase publica caja
    //Atributos (Caracteristicas)
    int ancho;
    int alto;
    int profundo;
    //Metodos y constructores (Acciones)
    public Caja (){ //Constructor 1 = vacio 
        
    }
    //Constructor con parametros
    public Caja(int ancho, int alto, int profundo){ //Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    public int calcularVolumen(){
        return ancho * alto * profundo;
    }
}
