package Patrones;

public class Pizzeria { //Factory pattern
    public Pizza smallPizza(){
        return new Pizza(6);
    }


    public Pizza mediumPizza(){
        return new Pizza(8);
    }

    public Pizza bigPizza(){
        return new Pizza(12);
    }


}
