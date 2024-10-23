package test;
import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("osvaldo", 57000.0, false);
        Persona perso2 = new Persona("Fran", 1000002.0, true);

        System.out.println("-------------------------");
        System.out.println("El primer objeto perso 2 es: ");
        System.out.println("los valores de perso2 modificados son: " + "su nombre es: " + perso2.getNombre() + " su sueldo es:" +  perso2.formatearSueldo() +" su estado boolean es: " + perso2.isEliminado());
        System.out.println("AHORA LE VUELVO A CAMBIAR LOS VALORES A PERSO2");

        perso2.setNombre("Edu");
        perso2.setSueldo(20000.0);
        perso2.setEliminado(false);
        System.out.println( "--------------------------");
        System.out.println("Los nuevos valores de perso2 son");
        System.out.println("los valores de perso2 son: " + "su nombre es: "+ perso2.getNombre()+ " " + " su sueldo es:" +  perso2.formatearSueldo() +" su estado boolean es: " + perso2.isEliminado());

                //modificar a traves de los metodos
        persona1.setNombre("juan pedro");
        //persona1.nombre = "juan ignacio"; // es mala practica modificar atributos o variables de clases
        //System.out.println("nombre es: " + persona1.nombre);// ERROR
        System.out.println("personal su nombre es: " + persona1.getNombre());
        System.out.println("persona1 su sueldo es: " + persona1.formatearSueldo());
        System.out.println("persona1 su booleano es: " + persona1.isEliminado());
        /* tarea: crear otro objeto de tipo Persona, asignar valores de manera inicial
        e imprimir, luego modificar sus valores y volver a imprimir
         */
        // A MODO EXTRA AGREGUE UNA FUNCION EN LA CLASE PARA MOSTRAR BIEN EL SUELDO
        //NOTA: INGRESAR BIEN LOS VALORES DOUBLE  CON PUNTO PARA DECIMALES.
    }
}
