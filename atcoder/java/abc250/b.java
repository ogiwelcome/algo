import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();
            for(int i=0; i< a*n; i++) {
                for(int j=0; j<b*n; j++) {
                    if(((i / a) + (j / b))%2 == 0 ) {
                        System.out.print(".");
                    } else {
                        System.out.print("#");
                    }
                }
                System.out.println();
            }
        }
    }
}