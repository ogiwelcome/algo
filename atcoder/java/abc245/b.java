import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int[] a = new int[n];
            for(int i=0; i<n; i++) {
                a[i] = sc.nextInt();
            }
            for(int i=0; i<=2001; i++) {
                Boolean flag = true;
                for(int j=0; j<n; j++) {
                    if(i == a[j]) {
                        flag = false;
                        break;
                    }
                }
                if(flag) {
                    System.out.println(i);
                    return;
                }
            }
        }
    }
}