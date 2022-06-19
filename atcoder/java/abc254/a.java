import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.next();
        String s = n.substring(n.length() - 2);
        System.out.println(s);
        sc.close();
    }
}