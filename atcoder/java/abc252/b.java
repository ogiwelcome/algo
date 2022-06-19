import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] a = new int[n];
            int[] aa = new int[n];
            int[] b = new int[k];
            for(int i=0; i<n; i++) {
                a[i] = sc.nextInt();
                aa[i] = a[i];
            }
            for(int i=0; i<k; i++) {
                b[i] = sc.nextInt();
            }
            Arrays.sort(a);
            for(int i=0; i<k; i++) {
                if(aa[b[i]-1] == a[n-1]) {
                    System.out.println("Yes");
                    return;
                }
            }
            System.out.println("No");

        }
    }
}