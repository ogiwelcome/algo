import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int k = sc.nextInt();
            long mod = 998244353;
            int[][] dp = new int[51][3010];
            dp[0][0] = 1;
            for(int i=0; i<n; i++) {
                for(int j=0; j<k; j++) {
                    for(int l=1; l<=m; l++) {
                        if(j+l <= k) {
                            dp[i+1][j+l] += dp[i][j];
                            dp[i+1][j+l] %= mod;
                        }
                    }
                }
            }
            long ans = 0;
            for(int i=0; i<=k; i++) {
                ans += dp[n][i];
                ans %= mod;
            }
            System.out.println(ans);
        }
    }
}