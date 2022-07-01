import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            char[] s = sc.next().toCharArray();
            for(int i=0; i<3; i++) {
                boolean flag = true;
                for(int j=0; j<s.length; j++) {
                    if(s[j]=='o' && j%3!=i) {
                        flag = false;
                    }else if(s[j]=='x' && j%3==i) {
                        flag = false;
                    }
                }
                if(flag) {
                    System.out.println("Yes");
                    return;
                }
            }
            System.out.println("No");
            return;
        }
    }
}