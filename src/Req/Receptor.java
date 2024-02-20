package Req;

public class Receptor extends Persona implements IReceptor{
    @Override
    public boolean comprarOrgano() {
        return false;
    }

    @Override
    public boolean requestOrgano() {
        return false;
    }
}
