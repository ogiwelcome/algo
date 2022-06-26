import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            double h = sc.nextDouble();
            System.out.println(Math.sqrt(h*(12800000+h)));
        }
    }
}