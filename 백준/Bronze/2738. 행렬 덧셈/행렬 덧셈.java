import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        int[][] array = new int[N][M];
        
        for(int i=0; i<2; i++) {
            for(int j=0; j<N; j++) {
               for(int k=0; k<M; k++) {
                   array[j][k] += sc.nextInt();
               } 
            }
        }
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                System.out.print(array[i][j] + " ");
            }
            System.out.println();
        }
        sc.close();
    }
}