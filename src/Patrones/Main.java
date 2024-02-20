package Patrones;

import PrincipiosSOLID.IFigura;
import QueueStack.*;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        //Main Single Factory
        Pizzeria p = new Pizzeria();
        Pizza grande = p.bigPizza();
        System.out.println(grande);

        //Main Singleton
        ConexionDB c1 = ConexionDB.obtenerConexion();
        ConexionDB c2 = ConexionDB.obtenerConexion(); //Private constructor so a new connection cannot be created
        System.out.println(c1.hashCode());
        System.out.println(c2.hashCode()); //Both have the same hashCode because they are the same object.

        //Main Builder
        Usuario u1 = Usuario.make("1").setEmail("hfj@gmail.com").setName("Jon").build();
        Usuario u2 = Usuario.make("2").setEmail("xx@gmail.com").setName("Winnie").build();
        System.out.println(u1);
        System.out.println(u2);

        //Prototype
        Enemy julio = new Enemy("julio.png",3,4,100);
        Enemy e2 = julio.clone();
        Enemy e3 = julio.clone();
        Enemy e4 = julio.clone();
        System.out.println(e3 + " " + e4);
        IConexionNoSQL mongo = new ConexionNoSQL();
        IConexion conexion = new Adapter(mongo);
        System.out.println(conexion.runQuery());

        //Queue and stack
        ILista s = new QStack(new Stack<>());
        ILista q = new QQueue(new LinkedList<>());

        s.add(1);
        s.add(2);
        s.add(3);
        System.out.println(s.rm());
        q.add(1);
        q.add(2);
        q.add(3);
        System.out.println(q.rm());

    }
}
