import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            long s = 0;
            for(int i=0; i<4*n-1; i++) {
                int a = sc.nextInt();
                s^=a;
            }
            System.out.println(s);
        }
    }
}