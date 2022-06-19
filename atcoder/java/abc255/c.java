import java.util.*;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long x = sc.nextLong();
        long a = sc.nextLong();
        long d = sc.nextLong();
        long n = sc.nextLong();
        long ans = Long.MAX_VALUE;
        if (d < 0) {
            a = a + d*(n-1);
            d = -d;
        }
        if (x <= a) {
            ans = Math.min(ans, a-x);
        }
        if (x >= a + d*(n-1)) {
            ans = Math.min(ans, x-a-d*(n-1));
        }
        if (a <= x && x <= a + d*(n-1)) {
            if (d == 0) {
                ans = 0;
            } else {
                ans = Math.min(ans, Math.min((x-a)%d, d-(x-a)%d));
            }
        }
        System.out.println(ans);
        sc.close();
    }
}