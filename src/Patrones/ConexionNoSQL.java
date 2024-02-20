package Patrones;

public class ConexionNoSQL implements IConexionNoSQL{
    @Override
    public void conexion() {
        System.out.println("Conexion mongo");
    }

    @Override
    public String executeSentence() {
        return "Sentencia mongo";
    }
}
