package spartaAlgorithmSheet;

public class _17_areaOrSquare {
    public static void main(String[] args) {

    }

    public int solution(int[][] dots) {
        int answer = 0;
        int width = 0;
        int height = 0;
        for (int i = 0; i < 3; i++) {
            if ((dots[3][0] - dots[i][0]) != 0) {
                width = Math.abs(dots[3][0] - dots[i][0]);
            }
            if ((dots[3][1] - dots[i][1]) != 0) {
                height = Math.abs(dots[3][1] - dots[i][1]);
            }
        }
        answer = width * height;
        return answer;
    }
}
