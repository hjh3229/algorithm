package programmers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MakeStars {
    public static void main(String[] args) {
        MakeStars makeStars = new MakeStars();
        int[][] line = {{2,-1,4}, {-2,-1,4}, {0,-1,1},{5,-8,-12},{5,8,12}};
        String[] test = makeStars.solution(line);
        System.out.println(Arrays.toString(test));
    }

    public String[] solution(int[][] line) {
        List<int[]> dots = getDots(line);
        int[] size = getSize(dots);
        System.out.println(size[1]);
        System.out.println(size[0]);
        String[] answer = new String[size[1]];
        for (int i = 0; i < size[1]; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < size[0]; j++) {
                boolean isStar = false;
                for (int k = 0; k < dots.size(); k++) {
                    int[] dot = dots.get(k);
                    if (j == size[2] + dot[0] && i == size[3] - dot[1]) {
                        sb.append("*");
                        isStar = true;
                        break;
                    }
                }
                if (!isStar) {
                    sb.append(".");
                }
            }
            answer[i] = sb.toString();
            System.out.println(answer[i]);
        }
        return answer;
    }

    public List<int[]> getDots(int[][] line) {
        List<int[]> dots = new ArrayList<>(); // 교점의 모임

        for (int i = 0; i < line.length - 1; i++) {
            int a = line[i][0];
            int b = line[i][1];
            int e = line[i][2];
            System.out.println("i =" + i);
            for (int j = line.length - 1; j > i; j--) {
                int c = line[j][0];
                int d = line[j][1];
                int f = line[j][2];
                System.out.println("j = " +j);
                // 두 직선이 평행하면 무시
                if ((double)(a / b) == (double) c / d) {
                    continue;
                }
//                 교점의 좌표가 정수가 아니면 무시
                if ((b * f - e * d) % (a * d - b * c) != 0 || (e * c - a * f) % (a * d - b * c) != 0) {
                    continue;
                }
                System.out.println(a +", "+ b +", "+ e +", "+ c +", "+ d +", "+ f);
                int getX = (b * f - e * d) / (a * d - b * c); // 교점의 x좌표
                int getY = (e * c - a * f) / (a * d - b * c); // 교점의 y좌표
                int dot[] = {getX, getY};
                System.out.println(Arrays.toString(dot));
                dots.add(dot);
            }
        }

        return dots;
    }

    public int[] getSize(List<int[]> dots) {
        int minX = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE;
        int minY = Integer.MAX_VALUE;
        int maxY = Integer.MIN_VALUE;

        for (int[] dot : dots) {
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

        int width = maxX - minX + 1;
        int height = maxY - minY + 1;
        int[] size = {width, height, maxX, maxY};
        return size;
    }
}
