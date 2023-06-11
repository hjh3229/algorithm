package spartaAlgorithmSheet;

public class _08_maxMaker {
    public static void main(String[] args) {
        int[] numbers = {1,19,0,54,81,30};
        _08_maxMaker maxMaker = new _08_maxMaker();
        System.out.println(maxMaker.solution(numbers));
        System.out.println(maxMaker.solution2(numbers));
    }

    public int solution(int[] numbers) {
        int answer = 0;
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i+1; j < numbers.length; j++) {
                int max = numbers[i] * numbers[j];
                if (max > answer) {
                    answer = max;
                }
            }
        }
        return answer;
    }

    public int solution2(int[] numbers) { // 멤버에 음수도 들어간다면
        int max = numbers[0];
        int maxPrev = 0;
        for(int i = 1; i< numbers.length; i++){
            if (max < numbers[i]) {
                maxPrev = max;
                max = numbers[i];
            } else if (maxPrev < numbers[i]) {
                maxPrev = numbers[i];
            }
        }
        int maxMulti = max * maxPrev;

        int min = numbers[0];
        int minPrev = 0;
        for (int i = 1; i < numbers.length; i++) {
            if (min > numbers[i]) {
                minPrev = min;
                min = numbers[i];
            } else if (maxPrev > numbers[i]) {
                maxPrev = numbers[i];
            }
        }
        int minMulti = min * minPrev;
        System.out.println(maxMulti);
        System.out.println(minMulti);

        if (maxMulti > minMulti) {
            return maxMulti;
        } else return minMulti;
    }
}
