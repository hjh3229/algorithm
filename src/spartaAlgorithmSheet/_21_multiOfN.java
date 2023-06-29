package spartaAlgorithmSheet;

import java.util.ArrayList;

public class _21_multiOfN {
    public static void main(String[] args) {

    }

    public int[] solution(int n, int[] numList) {
        ArrayList<Integer> nums = new ArrayList<>();
        for (int num : numList) {
            if (num%n == 0) {
                nums.add(num);
            }
        }
        int[] answer = new int[nums.size()];
        for (int i = 0; i < nums.size(); i++) {
            answer[i] = nums.get(i);
        }
        return answer;
    }
}
