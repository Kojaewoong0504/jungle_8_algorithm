import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<List<Integer>> g = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            g.add(new ArrayList<>());
        }

        int[] deg = new int[n];
        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            g.get(a).add(b);
            g.get(b).add(a);
            deg[a]++;
            deg[b]++;
        }

        Deque<Integer> q = new ArrayDeque<>();
        boolean[] removed = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (deg[i] == 1) {
                q.offer(i);
            }
        }

        while (true){
            int leafCount = q.size();
            if (leafCount <= 2){
                break;
            }

            for (int t = 0; t < leafCount; t++){
                int u = q.poll();
                if (removed[u]){
                    continue;
                }
                removed[u] = true;
                for (int v : g.get(u)){
                    if(removed[v]){
                        continue;
                    }
                    deg[v]--;
                    if (deg[v] == 1){
                        q.offer(v);
                    }
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (!removed[i]) {
                if (sb.length() > 0) sb.append(' ');
                sb.append(i);
            }
        }
        System.out.println(sb.toString());
    }
}
