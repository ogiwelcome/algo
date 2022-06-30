import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[][] g1 = new int[n][n];
            for(int i=0; i<m; i++) {
                int a = sc.nextInt();
                int b = sc.nextInt();
                g1[a-1][b-1] = g1[b-1][a-1] = 1;
            }
            int[][] g2 = new int[n][n];
            for(int i=0; i<m; i++) {
                int a = sc.nextInt();
                int b = sc.nextInt();
                g2[a-1][b-1] = g2[b-1][a-1] = 1;
            }
            int[] p = new int[n];
            for(int i=0; i<n; i++) {
                p[i] = i+1;
            }
            do {
                boolean flag = true;
                for(int i=0; i<n; i++) {
                    for(int j=0; j<n; j++) {
                        if(g1[i][j] != g2[p[i]-1][p[j]-1]) {
                            flag = false;
                        }
                    }
                }
                if(flag) {
                    System.out.println("Yes");
                    return;
                }
            } while(nextPermutation(p));
            System.out.println("No");
        }
    }
    static boolean nextPermutation(int[] arr) {
        int l = arr.length;
        int left = l-2;
        while(left>=0 && arr[left]>= arr[left+1])left--;
        if(left < 0) {
            return false;
        }
        int right = l-1;
        while(arr[left] >= arr[right]) {
            right--;
        }{
            int t = arr[left];
            arr[left]=arr[right];
            arr[right]=t;
        }
        left++;
        right = l-1;
        while (left < right) {
            int t = arr[left];
            arr[left]=arr[right];
            arr[right]=t;
            left++;
            right--;
        }
        return true;
    }
}