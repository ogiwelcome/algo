import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)){
            int h = sc.nextInt();
            int w = sc.nextInt();

            int x1 = -1;
            int x2 = -1;
            int y1 = -1;
            int y2 = -1;
            for(int i=0; i<h; i++) {
                char[] si = sc.next().toCharArray();
                for(int j=0; j<w; j++) {
                    if(si[j] == 'o') {
                        if(x1 == -1) {
                            x1 = i;
                            y1 = j;
                        } else {
                            x2 = i;
                            y2 = j;
                        }
                    }
                }
            }
            System.out.println(Math.abs(x1-x2) + Math.abs(y1-y2));
        }
    }
}