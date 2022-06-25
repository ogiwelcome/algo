import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            String[] s = new String[n];
            String[] t = new String[n];
            for(int i=0; i<n; i++) {
                s[i] = sc.next();
                t[i] = sc.next();
            }
            for(int i=0; i<n-1; i++) {
                for(int j=i+1; j<n; j++) {
                    if(s[i].equals(t[j]) || t[i].equals(t[j]) || t[i].equals(s[j])) {
                        System.out.println("No");
                        return;
                    }
                }
            }
            System.out.println("Yes");
        }
    }
}