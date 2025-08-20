import java.io.*;
import java.util.*;

public class Main {

    static boolean win(char[][] g, char me) {
        // rows
        for (int r = 0; r < 3; r++) if (g[r][0] == me && g[r][1] == me && g[r][2] == me) return true;
        // cols
        for (int c = 0; c < 3; c++) if (g[0][c] == me && g[1][c] == me && g[2][c] == me) return true;
        // diagonals
        if (g[0][0] == me && g[1][1] == me && g[2][2] == me) return true;
        if (g[0][2] == me && g[1][1] == me && g[2][0] == me) return true;
        return false;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder out = new StringBuilder();

        for (int tc = 1; tc <= t; tc++) {
            char[][] g = new char[3][3];
            for (int r = 0; r < 3; r++) {
                g[r] = br.readLine().toCharArray();
            }
            char me = br.readLine().charAt(0);
            outer:
            for (int r = 0; r < 3; r++) {
                for (int c = 0; c < 3; c++) {
                    if (g[r][c] == '-') {
                        g[r][c] = me;
                        if (win(g, me)) break outer;
                        g[r][c] = '-';
                    }
                }
            }

            out.append("Case ").append(tc).append(":\n");
            for (int r = 0; r < 3; r++) {
                out.append(g[r][0]).append(g[r][1]).append(g[r][2]).append('\n');
            }
        }
        System.out.print(out);

    }
}