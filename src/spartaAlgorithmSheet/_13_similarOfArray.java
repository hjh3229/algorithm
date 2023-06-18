package spartaAlgorithmSheet;

public class _13_similarOfArray {
    public static void main(String[] args) {
        _13_similarOfArray similarOfArray = new _13_similarOfArray();
        String[] s1 = {"n", "omg"};
        String[] s2 = {"m", "dot"};
        int test = similarOfArray.solution(s1, s2);
        System.out.println(test);
    }

    public int solution(String[] s1, String[] s2) {
        int count = 0;
        for (int i = 0; i < s1.length; i++) {
            for (int j = 0; j < s2.length; j++) {
                if (s1[i].equals(s2[j])) {
                    count++;
                }
            }
        }
        return count;
    }
}
