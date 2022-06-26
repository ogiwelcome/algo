import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int x = sc.nextInt();
            Set<Integer> set = new HashSet<Integer>();
            set.add(0);
            for(int i=0; i<n; i++) {
                Set<Integer> nxt = new HashSet<Integer>();
                int a = sc.nextInt();
                int b = sc.nextInt();
                for(int j: set) {
                    nxt.add(j+a);
                    nxt.add(j+b);
                }
                set = nxt;
            }
            if(set.contains(x)) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
    }
}