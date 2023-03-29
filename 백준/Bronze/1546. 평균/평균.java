import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
           
        float[] num = new float[sc.nextInt()];
        
        for(int i=0; i<num.length; i++) {
            num[i] = sc.nextInt();
        }
        
        float sum = 0;
        Arrays.sort(num);
        
        for(int i=0; i<num.length; i++){
            sum += ((num[i]/num[num.length-1])*100);
        }
        
        sc.close();
        System.out.println(sum/num.length);
    }
}