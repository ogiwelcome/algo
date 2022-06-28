import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            long n = sc.nextLong();
            if(-Math.pow(2,31) <= n && n < Math.pow(2, 31)) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
    }
}