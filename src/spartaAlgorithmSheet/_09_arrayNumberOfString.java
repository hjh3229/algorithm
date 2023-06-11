package spartaAlgorithmSheet;

import java.util.ArrayList;
import java.util.Arrays;

public class _09_arrayNumberOfString {
    public static void main(String[] args) {
        String my_string = "hjh3229";
        _09_arrayNumberOfString arrayNumberOfString = new _09_arrayNumberOfString();
        int[] solution = arrayNumberOfString.solution(my_string);
        for (int i = 0; i < solution.length; i++) {
            System.out.println(solution[i]);
        }
    }

    public int[] solution(String my_string) {
        ArrayList<Integer> numbers = new ArrayList<>();
        char[] stringArr = my_string.toCharArray();
        for (int i = 0; i < stringArr.length; i++) {
            int value = Character.getNumericValue(stringArr[i]);
            if (value <= 9) {
                numbers.add(value);
            }
        }
        int[] answer = new int[numbers.size()];
        for (int i = 0; i < numbers.size(); i++) {
            answer[i] = numbers.get(i);
        }
        Arrays.sort(answer);
        return answer;
    }
}
