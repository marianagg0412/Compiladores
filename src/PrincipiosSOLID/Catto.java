package PrincipiosSOLID;

public class Catto implements FelinoHome{

    @Override
    public String cazar() {
        return "rawr";
    }

    @Override
    public String maullar() {
        return "miau";
    }
/*
    @Override
    public String rugir() { //Cannot be here because cat's do not do this, ergo it cannot implement from feline.
        return null;
    }*/
}
