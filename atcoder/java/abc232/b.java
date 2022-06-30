import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            char[] s = sc.next().toCharArray();
            char[] t = sc.next().toCharArray();
            int k = (s[0]-t[0]+26)%26;
            for(int i=0; i<s.length; i++) {
                int d = (s[i]-t[i]+26)%26;
                if(k!=d) {
                    System.out.println("No");
                    return;
                }
            }
            System.out.println("Yes");
        }
    }
}