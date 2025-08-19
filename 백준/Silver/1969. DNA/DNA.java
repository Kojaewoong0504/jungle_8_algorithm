import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static String[] arr;

    static int idx(char c) {
        switch (c) {
            case 'A': return 0;
            case 'C': return 1;
            case 'G': return 2;
            default:  return 3; // 'T'
        }
    }

    static char ch(int k) {
        return "ACGT".charAt(k);
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new String[N];
        for (int i = 0; i < N; i++) {
            arr[i] = br.readLine().trim();
        }

        StringBuilder sb = new StringBuilder();
        int totalDist = 0;

        int[] cnt = new int[4];

        for (int col = 0; col < M; col++) {
            Arrays.fill(cnt, 0);
            for (int row = 0; row < N; row++) {
                cnt[idx(arr[row].charAt(col))]++;
            }

            int bestK = 0, bestCnt = cnt[0];
            for (int k = 1; k < 4; k++) {
                if (cnt[k] > bestCnt) {
                    bestCnt = cnt[k];
                    bestK = k;
                }
            }

            sb.append(ch(bestK));
            totalDist += (N - bestCnt);
        }

        System.out.println(sb.toString());
        System.out.println(totalDist);
    }
}
