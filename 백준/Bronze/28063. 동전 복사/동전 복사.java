import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine().trim());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());

        int cnt = 0;
        if (x > 1) cnt++;   // 왼쪽 경계로 확장 필요
        if (x < N) cnt++;   // 오른쪽 경계로 확장 필요
        if (y > 1) cnt++;   // 아래 경계로 확장 필요
        if (y < N) cnt++;   // 위 경계로 확장 필요

        System.out.println(cnt);
        


    }
}
