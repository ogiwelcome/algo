import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)){
            int n = sc.nextInt();
            HashSet<Integer> hs = new HashSet<>();
            for(int i=0; i<n ;i++){
                hs.add(sc.nextInt());
            }
            System.out.println(hs.size());
        }
    }
}