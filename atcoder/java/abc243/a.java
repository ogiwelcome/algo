import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int v = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            v = v%(a + b + c);
            if(v < a) {
                System.out.println("F");
            } else if (v < a+b) {
                System.out.println("M");
            } else {
                System.out.println("T");
            }
        }
    }
}