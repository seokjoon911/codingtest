import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] bucket = new int[N];

        for (int i=0; i<bucket.length; i++){
            bucket[i] = i+1;
        }     
        for(int i=0; i<M; i++){
            int a = sc.nextInt() - 1;
            int b = sc.nextInt() - 1;
        
            while(a < b){
                int temp = bucket[a];
                bucket[a++] = bucket[b];
                bucket[b--] = temp;
            }
        }
        for (int i=0; i<bucket.length; i++){
            System.out.print(bucket[i] + " ");
        }
        sc.close();
    }
}