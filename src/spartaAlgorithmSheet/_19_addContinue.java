package spartaAlgorithmSheet;

import java.util.Arrays;

public class _19_addContinue {
    public static void main(String[] args) {
        _19_addContinue addContinue = new _19_addContinue();
        int[] test = addContinue.solution(5, 5);
        System.out.println(Arrays.toString(test));
    }

    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        for (int i = 0; i < num; i++) {
            total -= i;
        }
        if (total%num == 0) {
            for (int i = 0; i < num; i++) {
                answer[i] = total / num + i;
            }
        }
        return answer;
    }
}
