import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            if(b-a == 1 || b-a == 9) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
    }
}