package spartaAlgorithmSheet;

public class _23_locate {
    public static void main(String[] args) {

    }

    public int[] solution(String[] keyInput, int[] board) {
        int x = 0;
        int y = 0;
        int width = board[0]/2;
        int height = board[1]/2;
        for (int i = 0; i < keyInput.length; i++) {
            switch (keyInput[i]) {
                case "up" :
                    if (y == height) break;
                    y++;
                    break;
                case "down" :
                    if (y == -height) break;
                    y--;
                    break;
                case "right" :
                    if (x == width) break;
                    x++;
                    break;
                case "left" :
                    if (x == -width) break;
                    x--;
                    break;
            }
        }
        int[] answer = {x,y};
        return answer;
    }
}
