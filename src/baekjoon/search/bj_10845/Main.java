package baekjoon.search.bj_10845;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Queue<Integer> answer = new LinkedList<>();

        int time = Integer.parseInt(br.readLine());
        int last = -1; // 마지막 수 조회 용
        for (int i = 0; i < time; i++) {
            String[] order = br.readLine().split(" ");
            switch (order[0]) {
                case "push" : answer.offer(Integer.parseInt(order[1]));
                last =Integer.parseInt(order[1]);
                break;
                case "pop" : if (answer.size() == 0) {
                    System.out.println(-1);
                } else {
                    System.out.println(answer.peek());
                    answer.poll();
                }
                break;
                case "size" : System.out.println(answer.size());
                break;
                case "empty" : if (answer.isEmpty()) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
                break;
                case "front" : if (answer.size() == 0) {
                    System.out.println(-1);
                } else {
                    System.out.println(answer.peek());
                }
                break;
                case "back" : if (answer.size() == 0) { // Deque를 사용하면 peekLast() 메서드로 쉽게 확인할 수 있으나 이 기능은 직접 구현해봤다.
                    System.out.println(-1);
                } else {
                    System.out.println(last);
                }
            }
        }
    }
}
