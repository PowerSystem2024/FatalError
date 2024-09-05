
package Clases;


public class PruebaPersona {
    public static void main(String[]args){
    
        Persona persona1;
        persona1 = new Persona(); // Llamamos al constructor
        persona1.nombre = "Luca";
        persona1.apellido = "Perez";
        persona1.obtenerInformacion();
        
    }
    
}
