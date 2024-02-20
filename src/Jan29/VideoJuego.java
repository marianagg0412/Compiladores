package Jan29;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.Objects;

public class VideoJuego {

    public VideoJuego(Integer id, String nombre, String desarrolladora, BigInteger vental) {
        this.id = id;
        this.nombre = nombre;
        this.desarrolladora = desarrolladora;
        this.vental = vental;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        VideoJuego that = (VideoJuego) o;
        return Objects.equals(id, that.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }

    private Integer id;
    private String nombre;
    private String desarrolladora;
    private BigInteger vental;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDesarrolladora() {
        return desarrolladora;
    }

    public void setDesarrolladora(String desarrolladora) {
        this.desarrolladora = desarrolladora;
    }

    public BigInteger getVental() {
        return vental;
    }

    public void setVental(BigInteger vental) {
        this.vental = vental;
    }

    @Override
    public String toString() {
        return "VideoJuego{" +
                "id=" + id +
                ", nombre='" + nombre + '\'' +
                ", desarrolladora='" + desarrolladora + '\'' +
                ", vental=" + vental +
                '}';
    }
}
