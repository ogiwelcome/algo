import java.util.*;

import javax.sound.sampled.Line;

class Main {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int[] x = new int[n];
            int[] y = new int[n];
            for(int i=0; i<n; i++) {
                x[i] = sc.nextInt();
                y[i] = sc.nextInt();
            }
            char[] s = sc.next().toCharArray();
            Map<Integer, Line> map = new HashMap<>();
            for(int i=0; i<n; i++) {
                Line line;
                if(map.containsKey(y[i])) {
                    line = map.get(y[i]);
                } else {
                    line = new Line();
                }
                if(s[i] == 'L') {
                    line.l = Math.max(line.l, x[i]);
                } else {
                    line.r = Math.min(line.r, x[i]);
                }
                if(line.r < line.l) {
                    System.out.println("Yes");
                    return;
                }
                map.put(y[i], line);
            }
            System.out.println("No");
        }
    }
    static class Line {
		int r = 1_000_000_001;
		int l = -1;
	}
}