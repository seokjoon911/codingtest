import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean[] student = new boolean[30];
        
        for(int i=0; i<28; i++){
            int n = sc.nextInt();
            student[n-1] = true;
        }
        for(int i=0; i<30; i++){
            if(student[i] != true) {
                System.out.println(i+1);
            }
        }
        sc.close();
    }
}