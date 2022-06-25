import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            String s = sc.next();
            String s2 = "0" + s.substring(0, 3);
            System.out.println(s2);
        }
    }
}