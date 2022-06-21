import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            String s = sc.next();
            if(s.equals(s.toLowerCase()) || s.equals(s.toUpperCase())) {
                System.out.println("No");
                return;
            }
            String[] ss = s.split("");
            Set<String> st = new HashSet<>();
            for(String si: ss) {
                if(!st.add(si)) {
                    System.out.println("No");
                    return;
                }
            }
            System.out.println("Yes");
        }
    }
}