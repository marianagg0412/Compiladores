package Patrones;

public class Adapter implements IConexion{
    private IConexionNoSQL nosql;

    public Adapter(IConexionNoSQL nosql) {
        this.nosql = nosql;
    }

    @Override
    public void conexion() {
        nosql.conexion();
    }

    @Override
    public String runQuery() {
        return nosql.executeSentence();
    }
}
