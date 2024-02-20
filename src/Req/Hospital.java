package Req;

public class Hospital implements IHospital{
    private IPersona[] gente;
    private IOrgano[] organos;


    @Override
    public boolean abrir() {
        return false;
    }

    @Override
    public boolean close() {
        return false;
    }
}
