import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            int[] idx = new int[n];
            int[] val = new int[n];
            for(int i=0; i<n; i++){
                idx[i] = i;
                val[i] = i;
            }
            for(int i=0; i<q; i++) {
                int x = sc.nextInt()-1;
                int idx1 = idx[x];
                int idx2 = (idx1 == n-1) ? idx1-1 : idx1+1;
                int tmp = val[idx2];
                idx[x] = idx2;
                idx[tmp] = idx1;
                val[idx1] = tmp;
                val[idx2] = x;
            }
            for(int i: val) {
                System.out.print((i+1) + " ");
            }
        }
    }
}