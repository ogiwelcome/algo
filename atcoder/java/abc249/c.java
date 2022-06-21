import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            String[] s = new String[n];
            for(int i=0; i<n; i++) {
                s[i] = sc.next();
            }
            int ans = 0;
            for(int i=0; i<(1<<n); i++) {
                int[] alpha = new int[26];
                for(int j=0; j<26; j++) {
                    alpha[j] = 0;
                }
                for(int j=0; j<n; j++) {
                    if(((i>>j)&1) == 1) {
                        for(int l=0; l<s[j].length(); l++) {
                            alpha[s[j].charAt(l) - 'a']++;
                        }
                    } 
                }
                int now = 0;
                for(int y=0; y<26; y++) {
                    if(alpha[y] == k) {
                        now++;
                    }
                }
                ans = Math.max(ans, now);
            }
            System.out.println(ans);
        }
    }
}