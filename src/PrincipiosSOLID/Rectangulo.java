package PrincipiosSOLID;

public class Rectangulo implements IFigura { //Single responsibility
    private float base;
    private float height;

    public Rectangulo(float base, float height) {
        this.base = base;
        this.height = height;
    }

    public float getBase() {
        return base;
    }

    public void setBase(float base) {
        this.base = base;
    }

    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }

    @Override
    public String toString() {
        return "Rectangulo{" +
                "base=" + base +
                ", height=" + height +
                '}';
    }
    @Override
    public double area(){
        return base*height;
    }

    @Override
    public float perimeter() {
        return (base*2) + (height*2);
    }

    @Override
    public String informacion() {
        return "Es un rectangulo" + base + " : " + height;
    }
}
