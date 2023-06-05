package spartaAlgorithmSheet;

import java.util.Arrays;

public class _03_doubleArray {
    public static void main(String[] args) {
        int[] array = {1, 41, -23, 100, 452, -234};

        for (int i = 0; i < array.length; i++) {
            array[i] *= 2;
        }
        System.out.println(Arrays.toString(array));
    }
}
