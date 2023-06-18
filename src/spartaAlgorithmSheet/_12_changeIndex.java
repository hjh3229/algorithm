package spartaAlgorithmSheet;

public class _12_changeIndex {
    public static void main(String[] args) {
        _12_changeIndex changeIndex = new _12_changeIndex();
        String test = changeIndex.solution("I love you", 3,6);
        System.out.println(test);
    }

    public String solution(String my_string, int num1, int num2) {
        String answer = "";

        int big = 0;
        int small = 0;
        if (num1 > num2) {
            big = num1;
            small = num2;
        } else {
            big = num2;
            small = num1;
        }

        for (int i = 0; i < small; i++) {
            answer += my_string.charAt(i);
        }
        answer += my_string.charAt(big);
        for (int i = small + 1; i < big; i++) {
            answer += my_string.charAt(i);
        }
        answer += my_string.charAt(small);
        for (int i = big + 1; i < my_string.length(); i++) {
            answer += my_string.charAt(i);
        }
        return answer;
    }
}
