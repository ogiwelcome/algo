import java.util.*;

class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int c = sc.nextInt();
        int[][] a = {
            {sc.nextInt(), sc.nextInt()},
            {sc.nextInt(), sc.nextInt()},
        };
        System.out.println(a[r-1][c-1]);
        sc.close();
    }
}