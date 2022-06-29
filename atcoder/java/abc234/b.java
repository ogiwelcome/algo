import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int[] x = new int[n];
            int[] y = new int[n];
            for(int i=0; i<n; i++) {
                x[i] = sc.nextInt();
                y[i] = sc.nextInt();
            }
            double ans = 0;
            for(int i=0; i<n; i++) {
                for(int j=i+1; j<n; j++) {
                    double d = (x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]);
                    d = Math.pow(d, 0.5);
                    ans = Math.max(ans, d);
                }
            }
            System.out.println(ans);
        }
    }
}