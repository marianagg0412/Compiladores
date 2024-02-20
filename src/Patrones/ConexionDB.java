package Patrones;

public class ConexionDB { //Singleton
    private static ConexionDB conexionDB;
    private ConexionDB(){

    }

    public static ConexionDB obtenerConexion(){
        if(conexionDB == null)
            conexionDB = new ConexionDB();

        return conexionDB;
    }

    public static ConexionDB desconectar(){
        return(conexionDB = null);
    }



}
