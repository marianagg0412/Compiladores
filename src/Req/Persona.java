package Req;

public class Persona implements IPersona{
    private String nombre;
    private int edad;
    private String id;
    private String tipoSangre;

    @Override
    public boolean signup() {
        return false;
    }

    @Override
    public boolean login() {
        return false;
    }

    @Override
    public boolean signout() {
        return false;
    }
}
