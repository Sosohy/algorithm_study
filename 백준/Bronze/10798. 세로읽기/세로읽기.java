import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        String[][] input = new String[5][15];
        String answer = "";
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < input.length; i++) {
            String str = sc.nextLine();
            input[i] = str.split("");
            //System.out.println(Arrays.toString(input[i]));
        }

        for (int i = 0; i < 15; i++) {
            for (int j = 0; j < input.length; j++) {
                if(input[j].length > i){
                    answer += input[j][i];
                }
            }
        }
        System.out.println(answer);
    }
}
