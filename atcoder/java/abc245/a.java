import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            int d = sc.nextInt();
            if(a < c) {
                System.out.println("Takahashi");
            } else if (a == c && b <= d) {
                System.out.println("Takahashi");
            } else {
                System.out.println("Aoki");
            }
        }
    }
}