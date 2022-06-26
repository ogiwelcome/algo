import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            long[][] dp = new long[n][11];
            for(int i=1; i<=9; i++) {
                dp[0][i]=1;
            }
            for(int i=1; i<n; i++) {
                for(int j=1; j<=9; j++) {
                    dp[i][j] += dp[i-1][j-1]+dp[i-1][j]+dp[i-1][j+1];
                    dp[i][j] %= 998244353;
                }
            }
            long ans = 0;
            for(int i=1; i<=9; i++) {
                ans += dp[n-1][i];
                ans %= 998244353;
            }
            System.out.println(ans);
        }
    }
}