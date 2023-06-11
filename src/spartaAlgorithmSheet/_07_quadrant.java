package spartaAlgorithmSheet;

public class _07_quadrant {
    public static void main(String[] args) {
        int[] dot = new int[2];
        _07_quadrant quadrant = new _07_quadrant();
        quadrant.solution(dot);
    }

    public int solution(int[] dot) {
        int answer;
        if (dot[0] > 0) {
            if (dot[1] > 0) {
                answer = 1;
            } else {
                answer = 4;
            }
        } else {
            if (dot[1] > 0) {
                answer = 2;
            } else {
                answer = 3;
            }
        }
        return answer;
    }
}

