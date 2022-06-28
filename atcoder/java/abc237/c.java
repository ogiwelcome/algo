import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            String s = sc.next();
            int i = 0;
            int n = s.length()-1;
            while(i<n && s.charAt(n)=='a') {
                n--;
                if(s.charAt(i)=='a'){
                    i++;
                }
            }
            int size = n;
            for(int j=i; j<=n; j++) {
                if(s.charAt(j)!=s.charAt(size)) {
                    System.out.println("No");
                    return;
                }
                size--;
            }
            System.out.println("Yes");
        }
    }
}