import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        int toRead = 2 * n;
        StringTokenizer st = null;
        HashSet<Integer> on = new HashSet<>();
        int maxCount = 0;

        while (toRead > 0) {
            if (st == null || !st.hasMoreTokens()) {
                String line = br.readLine();
                if (line == null) break;
                st = new StringTokenizer(line);
            }
            int x = Integer.parseInt(st.nextToken());

            if (on.contains(x)) {
                on.remove(x);
            }
            else {
                on.add(x);
            }

            maxCount = Math.max(maxCount, on.size());
            toRead--;
        }

        System.out.println(maxCount);
    }
}
