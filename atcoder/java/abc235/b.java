import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int[] h = new int[n];
            for(int i=0; i<n; i++) {
                h[i] = sc.nextInt();
            }
            for(int i=0; i<n-1; i++) {
                if(h[i] >= h[i+1]) {
                    System.out.println(h[i]);
                    return;
                }
            }
            System.out.println(h[n-1]);
        }
    }
}