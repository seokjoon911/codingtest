import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int[] array = new int[N];
        int M = sc.nextInt();
        
        for(int i=0; i<M; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();
            int ball = sc.nextInt();
            
            for(int j=A-1; j<B; j++) {
                array[j] = ball;
            }
        }
        for(int i=0; i<array.length; i++) {
            System.out.print(array[i] + " ");
        }   
        sc.close();
        
    }
}