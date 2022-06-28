import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            char[] s = sc.next().toCharArray();
            int a = sc.nextInt();
            int b = sc.nextInt();
            a--;
            b--;
            char tmp = s[a];
            s[a] = s[b];
            s[b] = tmp;
            System.out.println(s);
        }
    }
}