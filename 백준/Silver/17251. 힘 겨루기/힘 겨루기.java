import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int [] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) arr[i] = Integer.parseInt(st.nextToken());

        int[] prefMax = new int[n];
        prefMax[0] = arr[0];
        for (int i = 1; i < n; i++){
            prefMax[i] = Math.max(prefMax[i - 1], arr[i]);
        }

        int r = 0, b = 0;
        // 오른쪽 최댓값을 뒤에서부터 누적
        int rightMax = arr[n - 1]; // [n-1..n-1]
        for (int i = n - 2; i >= 0; i--) {
            int red = prefMax[i];     // [0..i]
            int blue = rightMax;      // [i+1..n-1]
            if (red > blue) r++;
            else if (red < blue) b++;
            // 같으면 아무 쪽도 증가 X (무승부)

            rightMax = Math.max(rightMax, arr[i]);
        }

        if (r > b) System.out.println("R");
        else if (r < b) System.out.println("B");
        else System.out.println("X");
    }
}
