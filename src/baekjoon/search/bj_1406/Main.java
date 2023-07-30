package baekjoon.search.bj_1406;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception{
        new Main().solution();
    }

    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] first = br.readLine().split("");
        List<String> answer = new ArrayList<>(Arrays.asList(first)); // 배열을 리스트화하는 방법
        int index = answer.size();
        int time = Integer.parseInt(br.readLine());
        for (int i = 0; i < time; i++) {
            String[] order = br.readLine().split(" ");
            if (order[0].equals("L")) {
                if (index != 0) {
                    index--;
                }
            } else if (order[0].equals("D")) {
                if (index != answer.size()) {
                    index++;
                }
            } else if (order[0].equals("B")) {
                if (index != 0) {
                    answer.remove(index-1);
                    index--;
                }
            } else if (order[0].equals("P")) {
                answer.add(index, order[1]);
                index++;
            }
        }
        for (int i = 0; i < answer.size(); i++) {
            sb.append(answer.get(i));
        }
        System.out.println(sb);
    }
}
