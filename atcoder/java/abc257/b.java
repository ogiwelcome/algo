import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int q = sc.nextInt();
            int[] a = new int[k+1];
            for(int i=0; i<k; i++) {
                a[i] = sc.nextInt();
            }
            a[k] = n+1;
            for(int i=0; i<q; i++) {
                int li = sc.nextInt();
                if(a[li]-a[li-1] > 1) {
                    a[li-1]++;
                }
            }
            for(int i=0; i<k; i++) {
                if(k-i==1) {
                    System.out.println(a[i]);
                } else {
                    System.out.print(a[i] + " ");
                }
            }
        }
    }
}