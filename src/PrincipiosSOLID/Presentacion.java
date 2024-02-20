package PrincipiosSOLID;

public class Presentacion {
    public void showFigure(IFigura a){
        System.out.println(a.informacion());
    }

    public void area(IFigura a){
        System.out.println("El area es: " + a.area());
    }

    public void perimetro(IFigura a){
        System.out.println("El perimetro es: " + a.perimeter());
    }
}
