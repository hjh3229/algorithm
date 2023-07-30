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
      k = Integer.parseInt(br.readLine());
      if (k == 0) {
        return;
      }
      S = new int[k];
      b = new boolean[k];
      String[] s = br.readLine().split(" ");
      for (int i = 0; i < k; i++) {
        S[i] = Integer.parseInt(s[i]);
      }
      solution(0, 0);
      System.out.println(sb);
      sb.setLength(0);
    }
  }

  public static void solution(int index, int start) throws Exception {
    if (index == 6) {
      for (int i = 0; i < 6; i++) {
        sb.append(a[i]).append(" ");
      }
      sb.append("\n");
      return;
    }
    for (int i = start; i < k; i++) {
      if (b[i]) continue;
      b[i] = true;
      a[index] = S[i];
      solution(index+1, i+1);
      b[i] = false;
    }
  }
}
