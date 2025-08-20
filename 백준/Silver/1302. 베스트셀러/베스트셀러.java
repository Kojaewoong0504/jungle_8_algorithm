import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            map.put(s, map.getOrDefault(s, 0) + 1);
        }

        String maxTitle = "";
        int maxCount = 0;
        for (Map.Entry<String, Integer> title : map.entrySet()) {
            String titleName = title.getKey();
            int count = title.getValue();
            if (count > maxCount || (count == maxCount && titleName.compareTo(maxTitle) < 0)){
                maxTitle = titleName;
                maxCount = count;
            }
        }
        System.out.println(maxTitle);
    }
}
