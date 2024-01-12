import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int hour = sc.nextInt();
        int minute = sc.nextInt();

        minute -= 45;
        if(minute < 0){
            if(hour == 0) hour = 24;
            hour--;
            minute += 60;
        }

        System.out.println(hour + " " + minute);
    }
}
