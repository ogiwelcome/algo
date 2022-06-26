import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            char[] s = sc.next().toCharArray();
            int[] w = new int[n];
            for(int i=0; i<n; i++) {
                w[i] = sc.nextInt();
            }
            TreeMap<Integer, Integer> map = new TreeMap<>();
            for(int i=0; i<n; i++) {
                if(s[i] == '0') {
                    map.put(w[i]+1, map.getOrDefault(w[i]+1, 0) + 1);
                } else {
                    map.put(w[i]+1, map.getOrDefault(w[i]+1, 0) - 1);
                    map.put(0, map.getOrDefault(0, 0) + 1);
                }
            }
            Iterator<Integer> it = map.keySet().iterator();
            int sum = 0;
            int max = 0;
            while(it.hasNext()) {
                max = Math.max(max, sum += map.get(it.next()));
            }
            System.out.println(max);
        }
    }
}