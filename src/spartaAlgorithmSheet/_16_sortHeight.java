package spartaAlgorithmSheet;

public class _16_sortHeight {
    public static void main(String[] args) {

    }

    public int solution(int[] array, int height) {
        int answer= 0;
        for (int others : array) {
            if (others > height) {
                answer++;
            }
        }
        return answer;
    }
}
