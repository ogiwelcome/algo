import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            if(n==1 || n>=5) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
    }
}