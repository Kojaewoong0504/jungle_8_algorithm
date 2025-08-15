
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main{
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder(4 * K + 3);
        sb.append("AKA");
        for (int i = 0; i < K; i++) {
            sb.append("RAKA");
        }

        System.out.println(sb.toString());
    }
}
