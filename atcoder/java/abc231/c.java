import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            int[] a = new int[n];
            for(int i=0; i<n; i++) {
                a[i] = sc.nextInt();
            }
            Arrays.sort(a);
            for(int i=0; i<q; i++) {
                int x = sc.nextInt();
                int l=-1;
                int r=n;
                while(r-l>1) {
                    int mid = (l+r)/2;
                    if(a[mid]>=x) {
                        r=mid;
                    } else {
                        l=mid;
                    }
                }
                System.out.println(n-r);
            }
        }
    }
}