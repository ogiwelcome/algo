import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            String s = sc.next();
            String ans = s;
            while(ans.length() < 6) {
                ans += s;
            }
            System.out.println(ans);
        }
    }
}