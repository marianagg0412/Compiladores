package PrincipiosSOLID;

public class Main {
        public static void main(String[] args) throws ETriangulo {

            IFigura r = new Rectangulo(3,4);
            IFigura t = new Triangulo(5,5,5,5,5);
            Presentacion p = new Presentacion();
            p.showFigure(r);
            p.showFigure(t);

            System.out.println("-------");

            ITeclado w = new Teclado();
            IMouse m = new Mouse();
            Computador x = new Computador(w,m);
            x.prender();
        }
}
