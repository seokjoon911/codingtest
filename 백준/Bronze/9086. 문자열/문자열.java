import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        String[] S = new String[N];
        
        for(int i=0; i<N; i++) {
            S[i] = sc.next();
        }
        for(int i=0; i<S.length; i++) {
            if(S[i].length() < 1) {
                System.out.println(S[i].charAt(S[i].length()+1));
            }
            else {
                System.out.print(S[i].substring(0,1));
                System.out.println(S[i].substring(S[i].length()-1, S[i].length()));
            }
        }
        sc.close();
    }
}