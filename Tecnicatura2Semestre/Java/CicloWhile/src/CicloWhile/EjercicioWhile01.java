package CicloWhile;

public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0; //Inferencia de tipos
        while(conteo < 3){
            System.out.println("Conteo = " + conteo);
            conteo++; //Vamos aumentando en uno la variable conteo 
        }
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        } while(contador <= 7);
        //Uso de las palabras Break y Continue juntos a las etiquetas (Labels)
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break ;
            }   
        }
        inicio:
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 != 0){
                continue inicio;//Esto significa ir a la siguiente iteracion
            }
            System.out.println("contando = " + contando);
        }
    }
}
