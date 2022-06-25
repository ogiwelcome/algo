import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            String ans = "1";
            for(int i=2; i<=n; i++) {
                ans = ans + " " + i + " " + ans;
            }
            System.out.println(ans);
        }
    }
}