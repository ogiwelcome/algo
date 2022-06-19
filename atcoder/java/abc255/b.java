import java.util.*;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] a = new int[k];
        Set<Integer> S = new HashSet<>();
        for(int i=0; i<k; i++){
            a[i] = sc.nextInt()-1;
            S.add(a[i]);
        }
        long[] x = new long[n];
        long[] y = new long[n];
        for(int i=0; i<n; i++) {
            x[i] = sc.nextInt();
            y[i] = sc.nextInt();
        }
        long ans = 0;
        for(int i=0; i<n; i++){
            if(S.contains(i)) continue;
            long tmp = Long.MAX_VALUE;
            for(int j:S){
                long dx = (x[j]-x[i])*(x[j]-x[i]);
                long dy = (y[j]-y[i])*(y[j]-y[i]);
                tmp = Math.min(tmp, dx + dy);
            }
            ans = Math.max(ans, tmp);
        }
        System.out.println(Math.sqrt(ans));
        sc.close();
    }
}