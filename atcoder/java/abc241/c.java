import java.util.*;

class Main {
    public static int a[][];
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            a = new int[n][n];
            for(int i=0; i<n; i++) {
                String s = sc.next();
                for(int j=0; j<n; j++) {
                    if(s.charAt(j)=='#') {
                        a[i][j] = 1;
                    } else {
                        a[i][j] = 0;
                    }
                }
            }
            for(int i=0; i<n; i++) {
                for(int j=0; j<n; j++) {
                    if(check(i,j,n)) {
                        System.out.println("Yes");
                        return;
                    }
                }
            }
            System.out.println("No");
        }
    }
    public static boolean check(int i, int j, int n) {
        int[] tmp = new int[4];
        for(int l=0; l<6; l++) {
            if(i+l<n) {
                tmp[0] += a[i+l][j];
            }
            if(j+l<n) {
                tmp[1] += a[i][j+l];
            }
            if(i+l<n && j+l<n && n-i>=6 && n-j>=6) {
                tmp[2] += a[i+l][j+l];
            }
            if(i+l<n && j-l>=0 && n-i>=6 && j>=5) {
                tmp[3] += a[i+l][j-l];
            }
        }
        if(tmp[0] >= 4 || tmp[1] >= 4 || tmp[2] >= 4 || tmp[3] >= 4) {
            return true;
        }
        return false;
    }
}