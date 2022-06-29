import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            int[] a = new int[n];
            for(int i=0; i<n; i++) {
                a[i] = sc.nextInt();
            }
            HashMap<Integer, List<Integer>> mp = new HashMap<Integer, List<Integer>>();
            for(int i=0; i<n; i++) {
                if(!mp.containsKey(a[i])) {
                    mp.put(a[i], new ArrayList<Integer>());
                }
                mp.get(a[i]).add(i+1);
            }
            for(int i=0; i<q; i++) {
                int x = sc.nextInt();
                int k = sc.nextInt();
                if(mp.containsKey(x) && k<=mp.get(x).size()) {
                    System.out.println(mp.get(x).get(k-1));
                } else {
                    System.out.println(-1);
                }
            }
        }
    }
}