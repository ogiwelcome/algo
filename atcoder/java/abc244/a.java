import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            String s = sc.next();
            System.out.println(s.substring(s.length()-1, s.length()));
        }
    }
}