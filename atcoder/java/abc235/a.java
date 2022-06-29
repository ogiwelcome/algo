import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int x = sc.nextInt();
            int a = x%10;
            int c = x/100;
            int b = (x-c*100-a)/10;
            System.out.println((a+b+c)*111);
        }
    }
}