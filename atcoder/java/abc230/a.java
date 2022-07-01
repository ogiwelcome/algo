import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            if(n>=42) {
                n++;
            }
            System.out.println("AGC"+String.format("%03d", n));
        }
    }
}