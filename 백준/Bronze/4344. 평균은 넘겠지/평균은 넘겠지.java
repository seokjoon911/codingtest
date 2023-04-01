import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int C = sc.nextInt();
        int[] score;
        
        for(int i=0; i<C; i++) {
            int N = sc.nextInt();
            score = new int[N];
            double sum = 0;
            
            for(int j=0; j<N; j++) {
                score[j] = sc.nextInt();
                sum += score[j];
            }
            
            double avg = (sum / N);
            double cnt = 0;
            
            for(int j=0; j<N; j++) {
                if(score[j] > avg) {
                    cnt++;
                }
            }
            
            System.out.println(String.format("%.3f%%", (cnt/N)*100));
        }
        sc.close();
    }
}