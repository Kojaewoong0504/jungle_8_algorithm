import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        long[] freq = new long[M];
        long prefix = 0;
        long answer = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            long a = Long.parseLong(st.nextToken());
            prefix += a;
            int r = (int)(prefix % M);
            if (r == 0) answer++;
            answer += freq[r];
            freq[r]++;
        }

        System.out.println(answer);
    }
}
