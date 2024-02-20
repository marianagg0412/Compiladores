package Jan29;

import java.util.*;

public class Sets {
    public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>();
        nums.add(1);
        nums.add(1);
        nums.add(4);
        nums.add(8);
        nums.add(80);
        nums.add(74);
        Set<Integer> set = new HashSet<>();
        //TreeSet: gives priority, slowest insertions O(n)
        //LinkedHashSet: FIFO O(log(n))
        //Set<String> n = new TreeSet<>();
        //Sorted set (pq essentially)
        set.addAll(nums);
        System.out.println(set);

        //Formas de recorrer
        /*for(Integer r: set){
            System.out.println(r);
        }*/
        set.forEach(System.out::println); //stream for map, count, etc.

    }
}
