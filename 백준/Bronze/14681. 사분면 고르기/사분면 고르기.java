import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int X = sc.nextInt();
        int Y = sc.nextInt();
        
        sc.close();
        
        if(0<X && 0<Y) {
            System.out.println(1);
        }
        else if(X<0 && 0<Y) {
            System.out.println(2);
        }
        else if(X<0 && Y<0) {
            System.out.println(3);
        }
        else {
            System.out.println(4);
        }
    }
}