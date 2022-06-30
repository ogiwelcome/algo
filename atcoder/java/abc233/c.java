import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            long x = sc.nextLong();
            List<Long> v = new ArrayList<>();
            v.add(1l);
            for(int i=0; i<n; i++) {
                int l = sc.nextInt();
                List<Long> t = new ArrayList<>();
                for(int j=0; j<l; j++) {
                    int aij = sc.nextInt();
                    for(long p: v) {
                        if(p*aij > x) {
                            continue;
                        }
                        t.add(p*aij);
                    }
                }
                v=t;
            }
            int ans = 0;
            for(long s: v) {
                if(s==x) ans++;
            }
            System.out.println(ans);
        }
    }
}