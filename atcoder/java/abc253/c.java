import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int Q = sc.nextInt();
            TreeMap<Integer, Integer> mp = new TreeMap<>();
            while(Q-->0) {
                int num = sc.nextInt();
                if(num == 1) {
                    int x = sc.nextInt();
                    mp.put(x, mp.getOrDefault(x, 0) + 1);
                } else if(num == 2) {
                    int x = sc.nextInt();
                    int c = sc.nextInt();
                    int val = mp.getOrDefault(x, 0);
                    val = Math.max(0, val-c);
                    if(val == 0) {
                        mp.remove(x);
                    } else {
                        mp.put(x, val);
                    }
                } else {
                    System.out.println(mp.lastKey() - mp.firstKey());
                }
            }
        }
    }
}