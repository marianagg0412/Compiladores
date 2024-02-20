package PrincipiosSOLID;

public class Teclado implements ITeclado{

    @Override
    public void conectar() {
        System.out.println("El teclado conectó");
    }
}
