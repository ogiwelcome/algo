import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int w = sc.nextInt();
            long[][] a = new long[n][2];
            long ans = 0;
		    for (int i=0; i<a.length; i++) {
			    for (int j=0; j<2; j++) {
				    a[i][j] = sc.nextLong();
			    }
		    }
            Arrays.sort(a, (x, y) -> (x[0] < y[0]) ? 1 : -1);
            for(int i=0; i<n; i++) {
                ans +=a[i][0]*Math.min(a[i][1], w);
                w -= Math.min(a[i][1], w);
                if(w <= 0) break;
            }
            System.out.println(ans);
        }
    }
}