package domain;


public class Persona {

    public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int aContadorPersona) {
        contadorPersona = aContadorPersona;
    }
    private int idPersona;
    private static int contadorPersona;
    private String nombre;
    
    public Persona(String nombre){
    this.nombre = nombre;
    //incremento contador por cada objeto nuevo
    Persona.contadorPersona++; // no uso thisí
    //asigno nuevo valor a la variable idPersona
    this.idPersona = Persona.contadorPersona;
    }

    public int getIdPersona() {
        return this. idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
    
    
    
    

}
