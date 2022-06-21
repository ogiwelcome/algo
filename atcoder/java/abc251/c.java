import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int oriMax = 0;
            int ans = 1;
            HashSet<String> hs = new HashSet<>();
            for(int i=0; i<n; i++) {
                String si = sc.next();
                int ti = sc.nextInt();
                if((!hs.contains(si)) && oriMax < ti) {
                    oriMax = ti;
                    ans = i+1;
                }
                hs.add(si);
            }
            System.out.println(ans);
        }
    }
}