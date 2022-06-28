import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            long n = sc.nextLong();
            long ans = 0;
            long p = 10;
            long q = 1;
            while(true) {
                long m = Math.min(n, p-1)-q+1;
                m %= 998244353;
                ans += (m*(m+1))/2;
                ans %= 998244353;
                if(p>n) break;
                p *= 10;
                q *= 10;
            }
            System.out.println(ans);
        }
    }
}