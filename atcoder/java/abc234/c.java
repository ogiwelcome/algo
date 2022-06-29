import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            long k = sc.nextLong();
            String s = Long.toBinaryString(k);
            System.out.println(s.replace("1", "2"));
        }
    }
}