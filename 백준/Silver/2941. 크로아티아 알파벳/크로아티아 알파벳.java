import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str[] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        
        String S = sc.nextLine();
        
        for(int i=0; i<str.length; i++) {
            if(S.contains(str[i])) {
                S = S.replace(str[i], "@");
            }
        }
        System.out.println(S.length());
        sc.close();
    }
}