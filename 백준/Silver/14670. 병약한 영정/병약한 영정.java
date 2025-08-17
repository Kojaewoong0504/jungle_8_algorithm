
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();
        String line;

        while (true) {
            // N 읽기 (EOF/빈줄 스킵)
            line = br.readLine();
            if (line == null) break;
            line = line.trim();
            if (line.isEmpty()) continue;
            int N = Integer.parseInt(line);

            // 증상 효능 -> 약 이름 매핑
            Map<Integer, Integer> effToMed = new HashMap<>(N * 2);
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int efficacy = Integer.parseInt(st.nextToken());
                int medName  = Integer.parseInt(st.nextToken());
                effToMed.put(efficacy, medName);
            }

            // R 읽기
            int R = Integer.parseInt(br.readLine().trim());
            for (int i = 0; i < R; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int L = Integer.parseInt(st.nextToken());

                // 질의 처리
                boolean ok = true;
                int[] meds = new int[L];
                for (int j = 0; j < L; j++) {
                    int symptom = Integer.parseInt(st.nextToken());
                    Integer med = effToMed.get(symptom);
                    if (med == null) ok = false;
                    meds[j] = (med == null ? -1 : med);
                }

                if (!ok) {
                    out.append("YOU DIED\n");
                } else {
                    for (int j = 0; j < L; j++) {
                        if (j > 0) out.append(' ');
                        out.append(meds[j]);
                    }
                    out.append('\n');
                }
            }
        }

        System.out.print(out.toString());
    }
}
