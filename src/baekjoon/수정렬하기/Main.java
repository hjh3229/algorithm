package baekjoon.수정렬하기;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        List<Integer> answer = new ArrayList<>();

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            answer.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(answer);

        for (Integer sorted : answer) {
            sb.append(sorted).append('\n');
        }
        System.out.println(sb);
    }
}
