import java.io.*;
import java.util.*;

public class Main {
    static int t, n;
    static int[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();
        t = Integer.parseInt(br.readLine().trim());
        for (int i = 0; i < t; i++) {
            n = Integer.parseInt(br.readLine().trim());
            arr = new int[n + 1];

            int filled = 0;
            StringTokenizer st = null;
            while (filled < n) {
                if (st == null || !st.hasMoreTokens()) {
                    String line = br.readLine();
                    if (line == null) break;
                    st = new StringTokenizer(line);
                    continue;
                }
                arr[++filled] = Integer.parseInt(st.nextToken());
            }

            int[] mark = new int[n + 1];
            int[] order = new int[n + 1];
            int cycleCount = 0;
            for (int s = 1; s <= n; s++) {
                if (mark[s] != 0) continue;

                int cur = s;
                int k = 0;

                while (mark[cur] == 0){
                    mark[cur] = s;
                    order[cur] = ++k;
                    cur = arr[cur];
                }

                if (mark[cur] == s) {
                    cycleCount += (k - order[cur] + 1);
                }
            }
            out.append(n - cycleCount).append("\n");
        }
        System.out.println(out.toString());
    }
}
