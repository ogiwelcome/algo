import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            long a = sc.nextLong();
            long b = sc.nextLong();
            while(a>0 && b>0) {
                if(a%10+b%10 >= 10) {
                    System.out.println("Hard");
                    return;
                }
                a/=10;
                b/=10;
            }
            System.out.println("Easy");
        }
    }
}