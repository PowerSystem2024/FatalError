package dominio;

public class Persona {
    private String nombre;
    private Double sueldo;
    private Boolean eliminado;

    public Persona() {
    }

    public Persona(String nombre, Double sueldo, Boolean eliminado) {
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }

    public String getNombre() {
        return nombre;
    }

    public Double getSueldo() {
        return sueldo;
    }

    public Boolean isEliminado(){
        return eliminado;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setSueldo(Double sueldo) {
        this.sueldo = sueldo;
    }

    public void setEliminado(Boolean eliminado) {
        this.eliminado = eliminado;
    }
}


