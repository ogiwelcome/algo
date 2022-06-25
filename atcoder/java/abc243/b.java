import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        int[] b = new int[n];
        for(int i=0; i<n; i++) {
            a[i] = sc.nextInt();
        }
        for(int i=0; i<n; i++) {
            b[i] = sc.nextInt();
        }
        int c1 = 0;
        int c2 = 0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if(a[i] == b[j]) {
                    if(i==j) {
                        c1++;
                    } else {
                        c2++;
                    }
                }
            }
        }
        System.out.println(c1);
        System.out.println(c2);
    }
}