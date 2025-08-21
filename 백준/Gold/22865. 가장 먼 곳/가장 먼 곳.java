import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Integer[] ground = new Integer[3];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 3; i++) {
            ground[i] = Integer.parseInt(st.nextToken());
        }

        int m = Integer.parseInt(br.readLine());

        ArrayList<int[]>[] graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) graph[i] = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph[a].add(new int[]{b, c});
            graph[b].add(new int[]{a, c});
        }

        long[] dA = dijkstra(n, graph, ground[0]);
        long[] dB = dijkstra(n, graph, ground[1]);
        long[] dC = dijkstra(n, graph, ground[2]);

        int ans = 1;
        long best = -1;
        for (int i = 1; i <= n; i++) {
            long s = Math.min(dA[i], Math.min(dB[i], dC[i]));
            if (s > best || (s == best && i < ans)) {
                best = s;
                ans = i;
            }
        }

        System.out.println(ans);

    }

    static long[] dijkstra(int n, ArrayList<int[]>[] g, int start) {
        long INF = Long.MAX_VALUE / 4;
        long[] dist = new long[n + 1];
        Arrays.fill(dist, INF);
        dist[start] = 0;

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.add(new long[]{0L, start});

        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long d = cur[0];
            int u = (int) cur[1];
            if (d != dist[u]) continue;

            for (int[] e : g[u]) {
                int v = e[0];
                int w = e[1];
                long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.add(new long[]{nd, v});
                }
            }
        }

        return dist;
    }
}
