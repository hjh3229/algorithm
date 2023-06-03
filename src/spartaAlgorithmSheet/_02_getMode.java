package spartaAlgorithmSheet;

import java.util.ArrayList;

public class _02_getMode {
    public static void main(String[] args) {
        int[] ints = {1,2,1,3,1,4,1,2,3,1};
        getMode(ints);
    }

    // 최빈값 구하는 메서드
    private static void getMode(int[] ints) {
        ArrayList<Integer> countInts = new ArrayList<>();
        for (int i = 0; i < checkInts(ints).size(); i++) {
            int count = 0;
            for (int j = 0; j < ints.length; j++) {
                // 확인된 숫자와 리스트 안에 숫자가 같으면 카운트 추가
                if (checkInts(ints).get(i).equals(ints[j])) {
                    count++;
                }
            }
            countInts.add(count);
        }

        // 카운트가 가장 큰 값의 숫자 확인하기 = 최빈값의 카운트
        int maxCount = 0;
        for (int i = 0; i < countInts.size(); i++) {
            if (countInts.get(i) > maxCount) {
                maxCount = countInts.get(i);
            }
        }

        System.out.println(checkInts(ints).get(countInts.indexOf(maxCount)) + " : " + maxCount + "회");
    }

    // 확인된 숫자 리스트 만들기
    private static ArrayList<Integer> checkInts(int[] ints) {
        ArrayList<Integer> checkedInts = new ArrayList<>();
        // 각각의 원소가 확인된 숫자 리스트에 없으면 추가
        for (int check : ints) {
            if (!checkedInts.contains(check)) {
                checkedInts.add(check);
            }
        }
        return checkedInts;
    }
}
