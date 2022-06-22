import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            long a = sc.nextLong();
            long b = sc.nextLong();
            long k = sc.nextLong();
            int c = 0;
            while(a < b) {
                a *= k;
                c++;
            }
            System.out.println(c);
        }
    }
}