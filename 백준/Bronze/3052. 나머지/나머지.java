import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);       
        int[] num = new int[10];
        boolean bl;
        int cnt = 0;
        
        for(int i=0; i<num.length; i++){
            num[i] = sc.nextInt() % 42;
        }      
        for(int i=0; i<num.length; i++) {
            bl = false;
            for(int j=i+1; j<num.length; j++) {
                if(num[i] == num[j]) {
                    bl = true;
                    break;
                }
            }
            if(bl == false) {
                cnt++;
            }
        }
        sc.close();
        System.out.println(cnt);
    }
}