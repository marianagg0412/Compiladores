package PrincipiosSOLID;

public class Computador {
    public ITeclado teclado;
    public IMouse mouse;

    public Computador(ITeclado teclado, IMouse mouse) {
        this.teclado = teclado;
        this.mouse = mouse;
    }

    public void prender(){
        this.teclado.conectar();
        this.mouse.conectar();
        System.out.println("PC on");
    }
}
