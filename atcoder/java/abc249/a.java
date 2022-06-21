import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            int d = sc.nextInt();
            int e = sc.nextInt();
            int f = sc.nextInt();
            int x = sc.nextInt();
            int distT = x/(a+c)*b*a+(x%(a+c)>a?a:(x%(a+c)))*b;		
		    int distA = x/(d+f)*e*d+(x%(d+f)>d?d:(x%(d+f)))*e;		
            String ret ="Takahashi";
		    if(distT==distA) {
			    ret ="Draw";
		    }else if(distA>distT) {
			    ret = "Aoki";
		    }
		    System.out.println(ret);
        }
    }
}