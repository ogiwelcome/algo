import java.util.*;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for(int i=0; i<n; i++){
            a[i] = sc.nextInt();
        }
        int p = 0;
        int[] cnt = {0, 0, 0};
        for(int i=0; i<n; i++){
            for(int j=2; j>=0; j--){
                if(cnt[j] == 1) {
                    cnt[j] = 0;
                    if(j+a[i] >= 3){
                        p++;
                    } else {
                        cnt[j+a[i]]=1;
                    }
                }
            }
            if(a[i]==4){
                p++;
            } else {
                cnt[a[i]-1] = 1;
            }
        }
        System.out.println(p);
        sc.close();
    }
}