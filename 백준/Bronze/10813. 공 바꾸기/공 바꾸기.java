import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int[] array = new int[N];
        int M = sc.nextInt();
        
        for(int i=0; i<N; i++) {
            array[i] = i+1;
        }
        for(int i=0; i<M; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();
            int temp = array[A-1];
            array[A-1] = array[B-1];
            array[B-1] = temp;
        }
        for(int i=0; i<N; i++) {
            System.out.print(array[i] + " ");
        }
        sc.close();
    }
}