import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            char[] s = sc.next().toCharArray();
            Arrays.sort(s);
            System.out.println(String.valueOf(s));
        }
    }
}