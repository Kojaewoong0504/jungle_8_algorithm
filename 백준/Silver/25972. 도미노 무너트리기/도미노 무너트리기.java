import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        long[][] dom = new long[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            dom[i][0] = Long.parseLong(st.nextToken());
            dom[i][1] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(dom, (x,y) -> Long.compare(x[0], y[0]));

        int chains = 1;
        for (int i = 1; i < n; i++) {
            long prevReach = dom[i-1][0] + dom[i-1][1];
            if (prevReach < dom[i][0]) {
                chains++;
            }
        }
        System.out.println(chains);
    }
}
