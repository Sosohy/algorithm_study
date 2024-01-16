import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int[] input = new int[10];

        for (int i = 0; i < input.length; i++) {
            int tmp = sc.nextInt();
            input[i] = tmp%42;
        }
        
        int cnt = 0;
        for (int i = 0; i < input.length; i++) {

            if(input[i] == -1) continue;

            for (int j = i+1; j < input.length; j++) {
                if(input[i] != -1 && input[i] == input[j])
                    input[j] = -1;
            }
            cnt++;
        }
        System.out.println(cnt);
    }
}
