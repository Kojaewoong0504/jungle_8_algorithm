import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        boolean [][] reach = new boolean[26][26];

        for (int i = 0; i < n; i++){
            String line = br.readLine();
            String[] parts = line.split(" ");
            int u = parts[0].charAt(0) - 'a';
            int v = parts[2].charAt(0) - 'a';
            reach[u][v] = true;
        }

        for (int k = 0; k < 26; k++) {
            for (int i = 0; i < 26; i++) {
                if (!reach[i][k]) continue;
                for (int j = 0; j < 26; j++) {
                    if (reach[k][j]) reach[i][j] = true;
                }
            }
        }

        int m = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            String line = br.readLine();
            String[] parts = line.split(" ");
            int u = parts[0].charAt(0) - 'a';
            int v = parts[2].charAt(0) - 'a';
            sb.append(reach[u][v] ? "T" : "F").append("\n");
        }

        System.out.println(sb.toString());
    }
}
