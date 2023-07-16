package baekjoon.search.bj_10828;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> answer = new ArrayList<>();

        int time = Integer.parseInt(br.readLine());

        for (int i = 0; i < time; i++) {
            String[] order = br.readLine().split(" ");
            switch (order[0]) {
                case "push" : answer.add(Integer.parseInt(order[1]));
                break;
                case "pop" : if (answer.size() == 0) {
                    System.out.println(-1);
                } else {
                    System.out.println(answer.get(answer.size() - 1));
                    answer.remove(answer.size() - 1);
                }
                break;
                case "size" : System.out.println(answer.size());
                break;
                case "empty" : if (answer.size() == 0) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
                break;
                case "top" : if (answer.size() == 0) {
                    System.out.println(-1);
                } else {
                    System.out.println(answer.get(answer.size() - 1));
                }
            }
        }
    }
}
