import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int x2 = sc.nextInt();
            int y2 = sc.nextInt();
            for(int dx=-3; dx<=3; dx++) {
                for(int dy=-3; dy<=3; dy++) {
                    int x3 = x1+dx;
                    int y3 = y1+dy;
                    if(dx*dx+dy*dy!=5) continue;
                    if((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3)==5) {
                        System.out.println("Yes");
                        return;
                    }
                }
            }
            System.out.println("No");
        }
    }
}