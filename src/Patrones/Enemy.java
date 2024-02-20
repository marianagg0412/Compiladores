package Patrones;

public class Enemy { //Prototype
    private String imagen;
    private int posx;
    private int posy;
    private int hp;

    public Enemy(String imagen, int posx, int posy, int hp) {
        this.imagen = imagen;
        this.posx = posx;
        this.posy = posy;
        this.hp = hp;
    }

    public String getImagen() {
        return imagen;
    }

    public void setImagen(String imagen) {
        this.imagen = imagen;
    }

    public int getPosx() {
        return posx;
    }

    public void setPosx(int posx) {
        this.posx = posx;
    }

    public int getPosy() {
        return posy;
    }

    public void setPosy(int posy) {
        this.posy = posy;
    }

    public int getHp() {
        return hp;
    }

    public void setHp(int hp) {
        this.hp = hp;
    }

    public Enemy(Enemy e){
        this.setHp(e.getHp()+2);
        this.setImagen(e.getImagen());
        this.setPosx(e.getPosx());
        this.setPosy(e.getPosy());
    }

    @Override
    public String toString() {
        return "Enemy{" +
                "imagen='" + imagen + '\'' +
                ", posx=" + posx +
                ", posy=" + posy +
                ", hp=" + hp +
                '}';
    }

    public Enemy clone(){
        return new Enemy(this);
    }
}
