import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int h = sc.nextInt();
            int w = sc.nextInt();
            int[][] at = new int[w][h];
            for(int i=0; i<h; i++) {
                for(int j=0; j<w; j++) {
                    at[j][i] = sc.nextInt();
                }
            }
            for(int[] ati: at) {
                for(int x: ati) {
                    System.out.print(x + " ");
                }
                System.out.println();
            }
        }
    }
}