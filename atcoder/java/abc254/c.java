import java.util.*;
class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            PriorityQueue<Integer>[] qs = new PriorityQueue[k];
            for(int i=0; i<k; i++) {
                qs[i] = new PriorityQueue<Integer>();
            }
            for(int i=0; i<n; i++) {
                int ai = sc.nextInt();
                qs[i%k].add(ai);
            }
            int prev = Integer.MIN_VALUE;
            for(int i=0; i<n; i++) {
                int num = qs[i%k].remove();
                if (prev <= num) {
                    prev = num;
                } else {
                    System.out.println("No");
                    return;
                }
            }
            System.out.println("Yes");
        }
    }
}