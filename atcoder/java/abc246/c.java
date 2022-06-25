import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int x = sc.nextInt();
            int[] a = new int[n];
            for(int i=0; i<n; i++) {
                a[i] = sc.nextInt();
            }
            for(int i=0; i<n; i++) {
                if(a[i] < x || k <= 0) {
                    continue;
                }
                int cnt = a[i]/x;
                cnt = Math.min(cnt, k);
                a[i] -= cnt*x;
                k -= cnt;
            }
            Arrays.sort(a);
            long ans = 0;
            if(n-1 >= k) {
                for(int i=0; i< n-k; i++) {
                    ans += a[i];
                }
            }
            System.out.println(ans);
        }
    }
}