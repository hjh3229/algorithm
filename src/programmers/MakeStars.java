package programmers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MakeStars {
    public static void main(String[] args) {
        MakeStars makeStars = new MakeStars();
        int[][] line = {{222, -358, 157}, {32, -15, 68}, {0, -1, 4},{5, 5, 10},{1, 5, 10}};
        String[] test = makeStars.solution(line);
        System.out.println(Arrays.toString(test));
    }

    public String[] solution(int[][] line) {
        List<int[]> dots = getDots(line); // 좌표들 조회
        int[] size = getSize(dots); // 크기 조회
        String[] answer = new String[size[1]]; // 세로의 길이를 기준으로 배열 생성
        for (int i = 0; i < size[1]; i++) {
            StringBuilder sb = new StringBuilder(); // 일괄 출력을 위해 StringBuilder 생성
            for (int j = 0; j < size[0]; j++) {
                boolean isStar = false; // 별을 찍었는지 확인
                for (int k = 0; k < dots.size(); k++) { // .을 찍고자 하는 위치가 좌표와 일치하는지 확인하는 구간
                    int[] dot = dots.get(k);
                    if ((dot[0] == size[2] + j) && (dot[1] == size[3] - i)) { // 좌표와 String[] 위치를 일치시키는 과정(위에서부터 점을 찍기 때문에 둘이 조금 다르다.)
                        sb.append("*"); // 별찍고
                        isStar = true; // 확인
                        break; // 해당 좌표에 별을 찍은게 확인이 되면 나머지를 확인할 필요가 없으므로
                    }
                }
                if (!isStar) { // 별을 안찍었으면 . 찍기
                    sb.append(".");
                }
            }
            System.out.println(sb);
            answer[i] = sb.toString();
        }
        return answer;
    }

    public List<int[]> getDots(int[][] line) { // 교점을 구하는 메서드 생성
        List<int[]> dots = new ArrayList<>(); // 교점의 모임 리스트

        for (int i = 0; i < line.length - 1; i++) { // 0번째부터 0,1,2, ... 비교
            int a = line[i][0]; // i번째 함수 x의 계수
            int b = line[i][1]; // i번째 함수 y의 계수
            int e = line[i][2]; // i번째 함수 상수항
            System.out.println("i = " + i);
            for (int j = line.length - 1; j > i; j--) { // 끝에서부터 n, n-1, n-2, ... 비교
                int c = line[j][0]; // j번째 함수 x의 계수
                int d = line[j][1]; // j번째 함수 y의 계수
                int f = line[j][2]; // j번째 함수 상수항
                System.out.println("j = " + j);
                // 두 직선이 평행하면 무시
                if (!(b == 0 || d == 0)) { // b나 d가 0이면 기울기 비교가 안되므로
                    if ((double) (a / b) == (double) c / d) { // double로 형변환 안하면 정수값끼리 비교하기 때문에 구하고자 하는 좌표가 무시될 수 있음
                        continue;
                    }
                }
                // b와 d가 둘 다 0이면 평행하므로 무시
                if (b == 0 && d == 0) {
                    continue;
                }
                // 교점의 좌표가 정수가 아니면 무시
                if ((b * f - e * d) % (a * d - b * c) != 0 || (e * c - a * f) % (a * d - b * c) != 0) {
                    continue;
                }
                int getX = (b * f - e * d) / (a * d - b * c); // 교점의 x좌표
                int getY = (e * c - a * f) / (a * d - b * c); // 교점의 y좌표
                int dot[] = {getX, getY}; // 교점
                System.out.println(Arrays.toString(dot));
                dots.add(dot); // 리스트에 추가
            }
        }
        return dots;
    }

    public int[] getSize(List<int[]> dots) { // 전체 가로 세로 크기를 구하는 메서드
        int minX = Integer.MAX_VALUE; // 가장 작은 x 좌표 (어떤 값이랑 비교하더라도 초기화 될 수 있도록 Integer.MAX_VALUE로 초기화)
        int maxX = Integer.MIN_VALUE; // 가장 큰 x 좌표 (어떤 값이랑 비교하더라도 초기화 될 수 있도록 Integer.MIN_VALUE로 초기화)
        int minY = Integer.MAX_VALUE; // 가장 작은 y 좌표
        int maxY = Integer.MIN_VALUE; // 가장 큰 y 좌표

        for (int[] dot : dots) { // 최대, 최소 좌표값 초기화
            if (dot[0] < minX) {
                minX = dot[0];
            }
            if (dot[0] > maxX) {
                maxX = dot[0];
            }
            if (dot[1] < minY) {
                minY = dot[1];
            }
            if (dot[1] > maxY) {
                maxY = dot[1];
            }
        }

        int width = maxX - minX + 1; // 가로의 길이
        int height = maxY - minY + 1; // 세로의 길이
        int[] size = {width, height, minX, maxY}; // 가로, 세로, 기준이 되기 위한 X 최솟값 Y 최댓값 저장
        System.out.println(Arrays.toString(size));
        return size;
    }
}
