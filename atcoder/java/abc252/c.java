import java.util.Scanner;

import java.util.*;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
		    int n=Integer.parseInt(sc.nextLine());
		    String[] in=new String[n];
		    for(int i=0;i<n;i++) in[i]=sc.nextLine();
		    int min=Integer.MAX_VALUE;
		    for(int i=0;i<10;i++) {
			    boolean[] arr=new boolean[1011];
			    Arrays.fill(arr, false);
			    int c=0;
			    for(int j=0;j<n;j++) {
				    char ch=String.valueOf(i).charAt(0);
				    int ind=in[j].indexOf(ch);
				    if(!arr[ind]) arr[ind]=true;
				    else {
					    while(arr[ind]) ind+=10;
					    arr[ind]=true;
				    }
				    if(c<ind) c=ind;
			    }
			    if(min>c) min=c;
		    }
		    System.out.println(min);
        }
    }
}