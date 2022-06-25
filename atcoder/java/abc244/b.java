import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            String t = sc.next();
            int x = 0;
            int y = 0;
            int d = 0;
            for(int i=0; i<n; i++) {
                if(t.charAt(i) == 'S') {
                    if(d==0)x++;
                    if(d==1)y--;
                    if(d==2)x--;
                    if(d==3)y++;
                } else {
                    d=(d+1)%4;
                }
            }
            System.out.printf("%d %d\n", x, y);
        }
    }
}