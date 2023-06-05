package spartaAlgorithmSheet;

import java.util.Arrays;

public class _04_reverseArray {
    public static void main(String[] args) {
        int[] array = {1, 41, -23, 100, 452, -234};
        int[] copyArray = array.clone();
        int length = array.length;

        for (int i = 0; i < length; i++) {
            array[i] = copyArray[length - i - 1];
        }
        System.out.println(Arrays.toString(array));
    }
}
