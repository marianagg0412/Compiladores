package Patrones;

public class Conexion implements IConexion{

    @Override
    public void conexion() {
        System.out.println("Conexion BD");
    }

    @Override
    public String runQuery() {
        return "Consulta SQL";
    }
}
