import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            String[] s = new String[n];
            for(int i=0; i<n; i++) {
                s[i] = sc.next();
            }
            HashSet<String> hs = new HashSet<String>();
            for(int j=0; j<m; j++) {
                String ti = sc.next();
                hs.add(ti);
            }
            for(int i=0; i<n; i++) {
                if(hs.contains(s[i])) {
                    System.out.println("Yes");
                } else {
                    System.out.println("No");
                }
            }

        }
    }
}