package spartaAlgorithmSheet;

public class _11_upperAndLower {
    public static void main(String[] args) {
        _11_upperAndLower upperAndLower = new _11_upperAndLower();
        String test = upperAndLower.solution("MyString");
        System.out.println(test);
    }

    public String solution(String my_string) {
        String answer = "";

        String upperCase = my_string.toUpperCase();
        for (int i = 0; i < my_string.length(); i++) {
            String upper = upperCase.valueOf(upperCase.charAt(i));
            String my = my_string.valueOf(my_string.charAt(i));
            if (upper.equals(my)) {
                answer += my.toLowerCase();
            } else {
                answer += upper;
            }
        }
        return answer;
    }
}
