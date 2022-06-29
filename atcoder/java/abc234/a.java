import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int t = sc.nextInt();
            System.out.println(f(f(f(t)+t)+f(f(t))));
        }
    }
    private static long f(long t) {
        return t*t+2*t+3;
    }
}