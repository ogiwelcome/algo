import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int h = sc.nextInt();
            int w = sc.nextInt();
            int r = sc.nextInt();
            int c = sc.nextInt();
            int ans = 4;
            if(r == 1) {
                ans--;
            }
            if(r == h) {
                ans--;
            }
            if(c == 1) {
                ans--;
            }
            if(c == w) {
                ans--;
            }
            System.out.println(ans);
        }
    }
}