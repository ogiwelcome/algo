import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            System.out.printf("%c\n", 'a' + (n-97));
        }
    }
}