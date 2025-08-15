import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String plain = br.readLine();        // 평문 (소문자 + 공백)
        String key   = br.readLine();        // 키 (소문자만)
        int m = key.length();

        StringBuilder sb = new StringBuilder(plain.length());

        for (int i = 0; i < plain.length(); i++) {
            char ch = plain.charAt(i);
            int k = key.charAt(i % m) - 'a' + 1; // 1..26 (1-based)

            if (ch == ' ') {
                // 공백은 그대로 출력, 키 인덱스는 i로 인해 자연스럽게 진행됨
                sb.append(' ');
                continue;
            }

            int p = ch - 'a' + 1;          // 1..26
            int c = p - k;                 // 1..26로 맞추기
            if (c <= 0) c += 26;

            sb.append((char)('a' + c - 1));
        }

        System.out.println(sb.toString());
    }
}
