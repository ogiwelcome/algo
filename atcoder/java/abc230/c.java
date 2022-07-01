import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            long n = sc.nextLong();
            long a = sc.nextLong();
            long b = sc.nextLong();
            long p = sc.nextLong();
            long q = sc.nextLong();
            long r = sc.nextLong();
            long s = sc.nextLong();
            for(long i=p; i<=q; i++) {
                for(long j=r; j<=s; j++) {
                    if(j==i-a+b || j==a+b-i) {
                        System.out.print("#");
                    } else {
                        System.out.print(".");
                    }
                }
                System.out.println();
            }
        }
    }
}