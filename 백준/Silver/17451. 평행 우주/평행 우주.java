import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        StringTokenizer st = new StringTokenizer(br.readLine());

        long[] v = new long[n];
        for (int i = 0; i < n; i++) v[i] = Long.parseLong(st.nextToken());

        long R = v[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            long vi = v[i];
            // R = ceil(R / vi) * vi  (오버플로 주의)
            long k = (R + vi - 1) / vi;   // ceilDiv
            R = k * vi;
        }
        System.out.println(R);
    }
}
