import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int[] array = new int[N];
        
        for(int i=0; i<N; i++) {
            array[i] = sc.nextInt();
        }
        
        sc.close();
        Arrays.sort(array);
        System.out.println(array[0] + " " + array[N-1]);
    }
}