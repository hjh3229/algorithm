package spartaAlgorithmSheet;

import java.util.ArrayList;

public class _10_shortString {
    public static void main(String[] args) {
        _10_shortString shortString = new _10_shortString();
        String test = shortString.solution("Hello World");
        System.out.println(test);
    }

    public String solution(String my_string) {
        ArrayList<String> answer = new ArrayList<>();
        for (int i = 0; i < my_string.length(); i++) {
            String addString = Character.toString(my_string.charAt(i));
            if (!answer.contains(addString)) {
                answer.add(addString);
            }
        }
        return String.join("",answer);
    }
}
