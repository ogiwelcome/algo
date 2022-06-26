import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[] a = new int[n];
            for(int i=0; i<n; i++) {
                a[i] = sc.nextInt();
            }
            HashMap<Integer, Integer> ca = new HashMap<>();
            for(int i=0; i<n; i++) {
                ca.put(a[i], ca.getOrDefault(a[i], 0)+1);
            }
            int[] b = new int[m];
            String res = "Yes";
            for(int i=0; i<m; i++) {
                b[i] = sc.nextInt();
                if((!ca.containsKey(b[i]) || ca.getOrDefault(b[i], 0) <= 0)) res = "No";
                else ca.put(b[i], ca.getOrDefault(b[i], 0)-1);
            }
            System.out.println(res);
        }
    } 
}