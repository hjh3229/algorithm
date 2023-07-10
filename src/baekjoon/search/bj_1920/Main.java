package baekjoon.search.bj_1920;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        HashSet<String> A = new HashSet<>();
        String[] a = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            A.add(a[i]);
        }
        int M = Integer.parseInt(br.readLine());
        String[] b = br.readLine().split(" ");
        for (int i = 0; i < M; i++) {
            if (A.contains(b[i])) {
                sb.append("1").append("\n");
            } else {
                sb.append("0").append("\n");
            }
        }

        System.out.println(sb);
    }
}
