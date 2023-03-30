import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String[] S = sc.next().split("");
        int N = sc.nextInt();
        
        System.out.println(S[N-1]);
    }
}