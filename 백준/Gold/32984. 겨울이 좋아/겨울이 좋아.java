import java.io.*;
import java.util.*;

public class Main {

    static int n;
    static long[] A, B;

    // ceil(a / b) for long
    static long ceilDiv(long a, long b) {
        return (a + b - 1) / b;
    }

    // D일 안에 모든 나무의 잎을 다 떨어뜨릴 수 있는가?
    // 각 나무 i에 필요한 최소 능력 사용 횟수 r_i = max(0, ceil(Ai/Bi) - D)
    // 모든 r_i 합이 D 이하면 가능 (하루 1번씩, 총 D번까지 사용 가능)
    static boolean feasible(long D) {
        long need = 0;
        for (int i = 0; i < n; i++) {
            long req = ceilDiv(A[i], B[i]) - D;
            if (req > 0) {
                need += req;
                if (need > D) return false; // 가지치기
            }
        }
        return need <= D;
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine().trim());
        A = new long[n];
        B = new long[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) A[i] = Long.parseLong(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) B[i] = Long.parseLong(st.nextToken());

        long hi = 0;
        for (int i = 0; i < n; i++) {
            hi = Math.max(hi, ceilDiv(A[i], B[i]));
        }
        long lo = 0;
        while (lo < hi) {
            long mid = (lo + hi) >>> 1;  // non-negative midpoint
            if (feasible(mid)) hi = mid;
            else lo = mid + 1;
        }
        System.out.println(lo);

    }

}
