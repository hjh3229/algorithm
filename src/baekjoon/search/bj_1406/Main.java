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

        String[] first = br.readLine().split("");
        List<String> answer = new ArrayList<>(Arrays.asList(first)); // 배열을 리스트화하는 방법
        int index = answer.size() - 1;
        int time = Integer.parseInt(br.readLine());
        for (int i = 0; i < time; i++) {
            String[] order = br.readLine().split(" ");
            switch (order[0]) {
                case "L" : if (index == 0) {
                    continue;
                } else {
                    index--;
                }
                break;
                case "D" : if (index == answer.size()) {
                    continue;
                } else {
                    index++;
                }
                break;
                case "B" : if (index == 0) {
                    continue;
                } else {
                    answer.remove(index);
                    index--;
                }
                break;
                case "P" : answer.add(index, order[1]);
                index++;
                break;
            }
        }
        for (int i = 0; i < answer.size(); i++) {
            System.out.print(answer.get(i));
        }
    }
}
