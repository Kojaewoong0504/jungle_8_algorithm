import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int [] visited = new int[n + 1];
        Arrays.fill(visited, -1);

        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.add(0);
        visited[0] = 0;

        while(!q.isEmpty()){
            int cur = q.poll();
            int d = visited[cur];

            int next1 = cur + 1;
            if (next1 <= n && visited[next1] == -1) {
                visited[next1] = d + 1;
                q.add(next1);
            }

            int next2 = cur + (cur / 2);
            if (next2 <= n && visited[next2] == -1) {
                visited[next2] = d + 1;
                q.add(next2);
            }
        }
        if (visited[n] != -1 && visited[n] <= k)  {
            System.out.println("minigimbob");
        } else {
            System.out.println("water");
        }
    }
}