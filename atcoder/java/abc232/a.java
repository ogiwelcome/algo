import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            String s = sc.next();
            int a = Integer.parseInt(s.substring(0,1));
            int b = Integer.parseInt(s.substring(2,3));
            System.out.println(a*b);
        }
    }
}