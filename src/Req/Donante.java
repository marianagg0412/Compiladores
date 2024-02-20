package Req;

public class Donante extends Persona implements IDonante{
    @Override
    public boolean publicarOrgano() {
        return false;
    }

    @Override
    public boolean enviarOrgano() {
        return false;
    }
}
