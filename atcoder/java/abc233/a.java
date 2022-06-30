import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            if(x >= y) {
                System.out.println(0);
            } else {
                int r = (y-x+9)/10;
                System.out.println(r);
            }
        }
    }
}