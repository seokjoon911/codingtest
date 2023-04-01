import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        double A = 0;
        double B = 0;

        for(int i=0; i<20; i++) {
            String title = sc.next();
            double score = sc.nextDouble();
            String grade = sc.next();
            
            switch(grade) {
                case "A+" :
                    A += score * 4.5;
                    B += score;
                    break;
                case "A0" :
                    A += score * 4.0;
                    B += score;
                    break;
                case "B+" :
                    A += score * 3.5;
                    B += score;
                    break;
                case "B0" :
                    A += score * 3.0;
                    B += score;
                    break;
                case "C+" :
                    A += score * 2.5;
                    B += score;
                    break;
                case "C0" :
                    A += score * 2.0;
                    B += score;
                    break;
                case "D+" :
                    A += score * 1.5;
                    B += score;
                    break;
                case "D0" :
                    A += score * 1.0;
                    B += score;
                    break;
                case "F" :
                    A += score * 0.0;
                    B += score;
                    break;
            }
        }
        System.out.printf("%.6f", A / B);
    }
}