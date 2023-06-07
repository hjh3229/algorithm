package spartaAlgorithmSheet;

public class _06_rockScissorsPaper {
    public static void main(String[] args) {
        _06_rockScissorsPaper a = new _06_rockScissorsPaper();
        System.out.println(a.solution("0525252052550"));
    }

    public String solution(String rsp){
        String[] rspStrings = rsp.split("");
        String answer = "";
        for (int i = 0; i < rsp.length(); i++) {
            if (rspStrings[i].equals("0")) {
                answer += "5";
            } else if (rspStrings[i].equals("2")) {
                answer += "0";
            } else if (rspStrings[i].equals("5")) {
                answer += "2";
            }
        }
        return answer;
    }
}
