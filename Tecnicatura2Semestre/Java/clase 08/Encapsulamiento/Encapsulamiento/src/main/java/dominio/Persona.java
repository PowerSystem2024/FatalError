package dominio;
import java.text.DecimalFormat;

public class Persona {
    //Atributos
    private String nombre;
    private Double sueldo;
    private Boolean eliminado;

//constructor con parametros
    public Persona(String nombre, Double sueldo, Boolean eliminado) {
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }
    //constructor por defecto
    public Persona() {
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Double getSueldo() {
        return sueldo;
    }
    public void setSueldo(Double sueldo) {
        this.sueldo = sueldo;
    }
    public Boolean isEliminado(){
        return eliminado;
    }
    public void setEliminado(Boolean eliminado) {
        this.eliminado = eliminado;
    }
    public String formatearSueldo() {
        if (sueldo == null) {
            return "Sueldo no asignado o vacio";
        }
        // Definir el formato para incluir el separador de miles con puntos
        DecimalFormat formato = new DecimalFormat("#,###.00");
        // Reemplazar las comas por puntos y devolver el sueldo formateado
        return formato.format(sueldo).replace(",", ".");
    }

    @Override
    public String toString() {
        return "Persona{" +
                "nombre='" + nombre + '\'' +
                ", sueldo=" + sueldo +
                ", eliminado=" + eliminado +
                '}';
    }
}
