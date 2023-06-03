package spartaAlgorithmSheet;

import java.util.Scanner;

public class _01_getQuotient {
    public static void main(String[] args) {
        _01_getQuotient get = new _01_getQuotient();
        System.out.println(get.getQuotient());
    }

    private int getQuotient() {
        Scanner sc = new Scanner(System.in);
        int firstNumber = sc.nextInt(); // 나눠지는 숫자
        int secondNumber = sc.nextInt(); // 나눌 숫자

        int quotient = firstNumber/secondNumber; // 타입이 int이므로 소수점을 버려진다.
        return quotient;
    }
}
