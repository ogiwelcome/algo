import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            TreeMap<String, Integer> tm = new TreeMap<>();
            for(int i=0; i<n; i++) {
                String s = sc.next();
                tm.put(s, tm.getOrDefault(s, 0)+1);
            }
            String res = "";
            int max = 0;
            for(String s: tm.keySet()) {
                if(tm.get(s) > max) {
                    res = s;
                    max = tm.get(s);
                }
            }
            System.out.println(res);
        }
    }
}