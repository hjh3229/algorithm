package spartaAlgorithmSheet;

import java.util.Arrays;

public class _22_toMultiDimensional {
    public static void main(String[] args) {

    }

    public int[][] solution(int[] num_list, int n) {
        int size = num_list.length;
        int[][] answer = new int[size/n][n];
        for (int i = 0; i < size; i++) {
            answer[i/n][i%n] = num_list[i];
        }
        return answer;
    }
}
