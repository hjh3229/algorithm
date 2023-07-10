package baekjoon.수찾기;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(br.readLine());
        }
        int M = Integer.parseInt(br.readLine());
        int[] B = new int[M];
        for (int i = 0; i < M; i++) {
            B[i] = Integer.parseInt(br.readLine());
        }
        int[] answer = new int[M];
        for (int i = 0; i < M; i++) {
            boolean match = false;
            int b = B[i];
            for (int j = 0; j < N; j++) {
                int a = A[j];
                if (a == b) {
                    match = true;
                    break;
                }
            }
            if (match) {
                answer[i] = 1;
            } else {
                answer[i] = 0;
            }
        }

        for (int i = 0; i < M; i++) {
            sb.append(answer[i]).append('\n');
        }

        System.out.println(sb);
    }
}
