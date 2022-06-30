import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int l = sc.nextInt()-1;
            int r = sc.nextInt()-1;
            String s = sc.next();
            String ans = s.substring(0, l) + new StringBuilder(s.substring(l, r+1)).reverse() + s.substring(r+1, s.length());
            System.out.println(ans);
        }
    }
}