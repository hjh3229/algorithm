package spartaAlgorithmSheet;

public class _14_findNum {
    public static void main(String[] args) {
        _14_findNum findNum = new _14_findNum();
        int test = findNum.solution(29183, 0);
        System.out.println(test);
    }

    public int solution(int num, int k) {
        int index = -1;
        int lenOfNum = String.valueOf(num).length();
        for (int i = 0; i < lenOfNum ; i++) {
            int digit = (int)((num%(Math.pow(10, i+1))/Math.pow(10,i)));
            if (digit == k) {
                index = lenOfNum-i;
            }
        }
        return index;
    }
}
