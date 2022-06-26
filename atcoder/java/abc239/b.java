import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            long x = sc.nextLong();
            long ans = Math.floorDiv(x, 10);
            System.out.println(ans);
        }
    }
}