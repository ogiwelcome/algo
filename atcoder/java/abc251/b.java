import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int w = sc.nextInt();
            int[] a = new int[n];
            for(int i=0; i<n; i++) {
                a[i] = sc.nextInt();
            }
            HashSet<Integer> cnt = new HashSet<>();
            for(int i=0; i<n; i++) {
                if(a[i] <= w) {
                    cnt.add(a[i]);
                }
            }
            for(int i=0; i<n; i++) {
                for(int j=i+1; j<n; j++) {
                    if(a[i] + a[j] <= w) {
                        cnt.add(a[i] + a[j]);
                    }
                }
            }
            for(int i=0; i<n; i++) {
                for(int j=i+1; j<n; j++) {
                    for(int k=j+1; k<n; k++) {
                        if(a[i] + a[j] + a[k] <= w) {
                            cnt.add(a[i] + a[j] + a[k]);
                        }
                    }
                }
            }
            System.out.println(cnt.size());
        }
    }
}