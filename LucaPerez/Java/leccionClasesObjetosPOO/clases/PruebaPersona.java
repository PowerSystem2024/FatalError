
package Clases;

import leccionClasesObjetos.src.main.java.Clases.Persona;

public class PruebaPersona {
    public static void main(String[]args){
    
        Persona persona1;
        persona1 = new Persona(); // Llamamos al constructor
        persona1.nombre = "Luca";
        persona1.apellido = "Perez";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2="+ persona2); // direccion de memoria alojada
        System.out.println("persona1="+ persona1);//imprime direccion de memoria
        persona2.obtenerInformacion();
        persona2.nombre = "Fiorella";
        persona2.apellido = "Gonzalez";
        persona2.obtenerInformacion();
    }
    
}
