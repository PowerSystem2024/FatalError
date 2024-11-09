
package test;

import domain.Cliente;
import domain.Empleado;
import java.util.Date;


public class TestHerencia {

 
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Pedro", 2000.00);
        System.out.println("empleado = " + empleado1);
         Cliente cliente1 = new Cliente( new Date(), true, "Lorena",'f', 32, "9 de julio");
        
    System.out.println("cliente = " + cliente1);
    }
 
   
    
}
