import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            String s1 = sc.next();
            String s2 = sc.next();
            if((s1.equals(".#") && s2.equals("#.")) || (s1.equals("#.") && s2.equals(".#"))) {
                System.out.println("No");
            } else {
                System.out.println("Yes");
            }
        }
    }
}