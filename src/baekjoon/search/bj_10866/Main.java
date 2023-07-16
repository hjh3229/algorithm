package baekjoon.search.bj_10866;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws Exception{
        new Main().solution();
    }

    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<Integer> answer = new LinkedList<>();

        int time = Integer.parseInt(br.readLine());

        for (int i = 0; i < time; i++) {
            String[] order = br.readLine().split(" ");
            switch (order[0]) {
                case "push_front" : answer.addFirst(Integer.parseInt(order[1]));
                break;
                case "push_back" : answer.addLast(Integer.parseInt(order[1]));
                break;
                case "pop_front" : if (answer.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(answer.peekFirst());
                    answer.removeFirst();
                }
                break;
                case "pop_back" : if (answer.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(answer.peekLast());
                    answer.removeLast();
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
                case "front" : if (answer.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(answer.peekFirst());
                }
                break;
                case "back" : if (answer.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(answer.peekLast());
                }
            }
        }
    }
}
