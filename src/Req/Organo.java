package Req;
public class Organo implements IOrgano{
    private boolean isDisponible;

    @Override
    public boolean transplantarse() {
        return false;
    }
}
