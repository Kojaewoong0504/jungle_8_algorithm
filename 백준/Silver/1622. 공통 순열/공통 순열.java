import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a, b;
        
        while ((a = br.readLine()) != null && (b = br.readLine()) != null) {
            int[] countA = new int[26];
            int[] countB = new int[26];

            for (char c : a.toCharArray()) countA[c - 'a']++;
            for (char c : b.toCharArray()) countB[c - 'a']++;

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 26; i++) {
                int common = Math.min(countA[i], countB[i]);
                for (int j = 0; j < common; j++) {
                    sb.append((char)('a' + i));
                }
            }

            System.out.println(sb.toString());
        }
    }
}
