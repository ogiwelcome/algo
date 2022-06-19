import java.util.*;

class Main {
    public static void main(String[] args){
        try (Scanner sc = new Scanner(System.in)) {
            double n = sc.nextDouble();
            System.out.println((int)Math.pow(2.0, n));
        }
    }
}