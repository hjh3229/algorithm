package spartaAlgorithmSheet;

import java.util.Arrays;

public class _15_sortArr {
    public static void main(String[] args) {
        _15_sortArr sortArr = new _15_sortArr();
        String test = sortArr.solution("HelloWorld");
        System.out.println(test);
    }

    public String solution(String my_string) {
        String low = my_string.toLowerCase();
        char[] sort = low.toCharArray();

        int length = sort.length;

        for (int i = 0; i < length - 1; i++) {
            for (int j = 0; j < length - i - 1; j++) {
                if (sort[j] > sort[j + 1]) {
                    char temp = sort[j];
                    sort[j] = sort[j + 1];
                    sort[j + 1] = temp;
                }
            }
        }

        String answer = new String(sort);
        return answer;
    }
}
