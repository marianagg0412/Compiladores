package Patrones;

public class Pizza { //Simple factory
    private int cantidadRebanadas;

    public Pizza(int cantidadRebanadas) {
        this.cantidadRebanadas = cantidadRebanadas;
    }

    public int getCantidadRebanadas() {
        return cantidadRebanadas;
    }

    public void setCantidadRebanadas(int cantidadRebanadas) {
        this.cantidadRebanadas = cantidadRebanadas;
    }

    @Override
    public String toString() {
        return "Pizza{" +
                "cantidadRebanadas=" + cantidadRebanadas +
                '}';
    }
}
