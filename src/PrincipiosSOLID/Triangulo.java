package PrincipiosSOLID;

public class Triangulo implements IFigura {
    private float base;
    private float height;
    private float lado1;
    private float lado2;
    private float lado3;

    public Triangulo(float base, float height,float lado1, float lado2, float lado3) throws ETriangulo {
        this.base = base;
        this.height = height;
        if(!isValid(lado1,lado2,lado3)) {
            this.lado1 = lado1;
            this.lado2 = lado2;
            this.lado3 = lado3;
        } else{
            throw new ETriangulo("Not valid");
        }
    }

    public boolean isValid(float l1, float l2, float l3){
        return l1 + l2 <= l3 && l2 + l3 <= l1 && l1 + l3 <= l2;
    }

    public float getLado1() {
        return lado1;
    }

    public void setLado1(float lado1) {
        this.lado1 = lado1;
    }

    public float getLado2() {
        return lado2;
    }

    public void setLado2(float lado2) {
        this.lado2 = lado2;
    }

    public float getLado3() {
        return lado3;
    }

    public void setLado3(float lado3) {
        this.lado3 = lado3;
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
    public double area() {
        return (base*height)/2;
    }

    @Override
    public float perimeter() {
        return lado1+lado2+lado3;
    }

    @Override
    public String informacion() {
        return "Es un triangulo" + base + " : " + height + " : " + lado1 + " : " + lado2 + " : " + lado3;
    }

}
