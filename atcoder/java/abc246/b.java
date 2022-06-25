import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            double a = sc.nextInt();
            double b = sc.nextInt();
            double d = Math.sqrt(a*a + b*b);
            System.out.println(a/d + " " + b/d);
        }
    }
}