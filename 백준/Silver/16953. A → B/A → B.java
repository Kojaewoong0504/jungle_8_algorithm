import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long A = Long.parseLong(st.nextToken());
        long B = Long.parseLong(st.nextToken());

        long steps = 0;

        while (B > A) {
            if (B % 10 == 1) {        // ...1이면 1 제거
                B /= 10;
            } else if (B % 2 == 0) {  // 짝수면 2로 나눔
                B /= 2;
            } else {
                System.out.println(-1);
                return;
            }
            steps++;
        }

        if (B == A) {
            System.out.println(steps + 1); // 문제: 연산 횟수 + 1 출력
        } else {
            System.out.println(-1);
        }

    }
}
