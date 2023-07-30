package baekjoon.backtracking.bj_6603;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
  static StringBuilder sb = new StringBuilder();
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static int k;
  static int[] S;
  static int[] a = new int[6];
  static boolean[] b;
  public static void main(String[] args) throws Exception {
    while (true) {
      String[] s = br.readLine().split(" ");
      k = Integer.parseInt(s[0]);
      if (k == 0) {
        return;
      }
      S = new int[k];
      b = new boolean[k];

      for (int i = 1; i <= k; i++) {
        S[i-1] = Integer.parseInt(s[i]);
      }
      solution(0, 0);
      System.out.println(sb);
      sb.setLength(0);
    }
  }

  public static void solution(int index, int start) throws Exception { // 백트래킹이 시작하는 시점은 6번째 자리 이전에 마지막 숫자를 넣었을 때
    if (index == 6) { // index는 숫자를 넣은 위치이므로 6번째 자리에 숫자를 넣으면 출력
      for (int i = 0; i < 6; i++) {
        sb.append(a[i]).append(" ");
      }
      sb.append("\n");
      return;
    }
    for (int i = start; i < k; i++) { // start는 b[] 내에서 비교를 시작할 위치
      if (b[i]) continue;
      b[i] = true;
      a[index] = S[i];
      sb.append(index+1 + " ");
      sb.append(i+1);
      sb.append("\n");
      solution(index+1, i+1);
      b[i] = false;
    }
  }
}
