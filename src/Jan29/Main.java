package Jan29;

import java.lang.reflect.Array;
import java.math.BigInteger;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        VideoJuego h1 = new VideoJuego(1, "Zelda BOTW", "Nintendo", new BigInteger("100"));
        VideoJuego h2 = new VideoJuego(2, "Zelda TOK", "Nintendo", new BigInteger("1000"));
        VideoJuego h3 = new VideoJuego(1, "Mario Wonder", "Nintendo", new BigInteger("100"));
        VideoJuego h4 = new VideoJuego(31, "Otro", "Nintendo", new BigInteger("100"));

        Set<VideoJuego> s = new HashSet<>();
        s.add(h1);
        s.add(h2);
        s.add(h3);
        s.add(h4);
        //s.forEach(System.out::println);

        List<VideoJuego> filt = s.stream().filter(e -> !e.getDesarrolladora().equalsIgnoreCase("Nintendo")).toList();
        //or using .forEach() right away to sout.
        System.out.println(filt);

        System.out.println("-------");

        //?
        List<String> fruits = Arrays.asList("apple", "banana", "cherry","orange");

        //old
        for(String l: fruits){
            if(l.contains("a"))
                System.out.println(l);
        }
        System.out.println();
        //functional programming
        //filtering and mapping
        List<String> filtered = fruits.stream().filter(c -> c.contains("a")).
                filter(d -> d.startsWith("b")).map(e -> e.toUpperCase()).toList();
        System.out.println(filtered);

        List<Integer> numbers = Arrays.asList(3,4,3,2,45,21);
        List<Integer> mapped = numbers.stream().map(e -> e*2).toList();
        System.out.println(mapped);

        System.out.println("-------");

        //?
        VideoJuego v1 = new VideoJuego(6, "Hollow knight", "Cherry", new BigInteger("100000"));
        VideoJuego v2 = new VideoJuego(2, "Fortnite", "Epic", new BigInteger("331"));
        VideoJuego v3 = new VideoJuego(1, "Fifa 23", "EA", new BigInteger("4585"));
        VideoJuego v4 = new VideoJuego(1, "Mario Kart 64", "Nintendo", new BigInteger("1458"));
        List<VideoJuego> juegos = Arrays.asList(v1,v2,v3,v4);
        List<VideoJuego> organized = juegos.stream().
                sorted(Comparator.comparing(VideoJuego::getId).reversed().
                        thenComparing(VideoJuego::getNombre)).toList();
        System.out.println(organized);

        System.out.println("-------");

        //
        List<Integer> nums = Arrays.asList(1,3,4,3,43221,4234);
        int sum = nums.stream().filter(q -> q%2 == 0).reduce(0, Integer::sum); //identity = starting point
        Optional<Integer> max = nums.stream().max(Integer::compare); //can be null
        // could be used when fetching from a db, and it returns no results.
        System.out.println(sum);
        System.out.println(max.get());
        List<String> words = Arrays.asList("Java", "is", "fun","and", "useful");
        Map<Integer, List<String>> groupedByLength = words.stream().
                collect(Collectors.groupingBy(String::length));
        System.out.println(groupedByLength.values());

        long odd = nums.stream().filter(r -> r%2!= 0).count();
        System.out.println(odd);

        System.out.println("-------");





    }
}
