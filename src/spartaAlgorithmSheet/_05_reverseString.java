package spartaAlgorithmSheet;

public class _05_reverseString {
    public static void main(String[] args) {
        _05_reverseString a = new _05_reverseString();
        System.out.println(a.solution("string"));
    }
    public String solution(String my_string) {
        char[] my_char = my_string.toCharArray();
        for (int i = 0; i < my_char.length; i++) {
            my_char[i] = my_string.charAt(my_char.length -i - 1);
        }
        String answer = new String(my_char);
        return answer;
    }
}
