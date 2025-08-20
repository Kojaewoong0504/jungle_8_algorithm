import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String [][] records = new String[n][2];
        Set<String> set = new TreeSet<>();
        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split(" ");
            records[i][0] = line[0];
            records[i][1] = line[1];
            if (records[i][1].equals("enter")) set.add(records[i][0]);
            else set.remove(records[i][0]);
        }

        String[] orderedName = set.toArray(new String[set.size()]);
        for (int i = orderedName.length - 1; i >= 0; i--) {
            System.out.println(orderedName[i]);
        }


    }
}
