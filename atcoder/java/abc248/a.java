import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            String a = sc.next();
            for(int i=0; i<=9; i++) {
                if(a.contains(Integer.toString(i))){
                    continue;
                } else {
                    System.out.println(i);
                }
            }
        }
    }
}