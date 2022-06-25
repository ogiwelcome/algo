import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] a = new int[n];
            for(int i=0; i<n; i++) {
                a[i] = sc.nextInt();
            }
            int[] b = new int[n];
            for(int i=0; i<n; i++) {
                b[i] = sc.nextInt();
            }
            var dp = new boolean[n];
            var ep = new boolean[n];
            dp[0] = true;
            ep[0] = true;
            for(int i=1; i<n; i++) {
                if(dp[i-1] && Math.abs(a[i-1]-a[i]) <= k) {
                    dp[i] = true;
                } else if(ep[i-1] && Math.abs(b[i-1]-a[i]) <= k) {
                    dp[i] = true;
                }
                if(dp[i-1] && Math.abs(a[i-1]-b[i]) <= k) {
                    ep[i] = true;
                } else if(ep[i-1] && Math.abs(b[i-1]-b[i]) <= k) {
                    ep[i] = true;
                }
            }
            if(dp[n-1] || ep[n-1]) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
    }
}