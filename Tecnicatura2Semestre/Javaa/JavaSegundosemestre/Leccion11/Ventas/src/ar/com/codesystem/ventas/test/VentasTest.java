
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500);
        Producto producto2 = new Producto("Campera", 30000.00);
        Producto producto3 = new Producto("Buzo", 50000.00);
        Producto producto4 = new Producto("Remera", 10000.00);
        Producto producto5= new Producto("Zapatillas", 90000.00);
        Producto producto6= new Producto("Medias", 5000.00);
        
        Orden orden1 = new Orden();
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();

        //Tarea
        //Crear mas objetos de tipo Producto
        //Crear mas objetos de tipo Orden
        
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.mostrarOrden();
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto5);
        orden3.agregarProducto(producto6);
        orden3.mostrarOrden();
        
    }
}
