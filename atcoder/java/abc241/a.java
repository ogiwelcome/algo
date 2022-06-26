import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int[] a = new int[10];
            for(int i=0; i<10; i++) {
                a[i] = sc.nextInt();
            }
            int b = 0;
            b = a[b];
            b = a[b];
            b = a[b];
            System.out.println(b);
        }
    }
}