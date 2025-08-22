
import java.util.Scanner;
public class Main {
    public String homework(String a, int la, String b, int lb, String c) {
        StringBuilder sb = new StringBuilder(a);
        for (int i = 0; i < lb; i++) {
            if (c.charAt(i) == 'D') {
                sb.append(b.charAt(i));
            } else {
                sb.insert(0, b.charAt(i));
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int lenA = sc.nextInt();
            String a = sc.next();
            int lenB = sc.nextInt();
            String b = sc.next();
            String c = sc.next();

            Main obj = new Main();
            System.out.println(obj.homework(a, lenA, b, lenB, c));
        }
    }
}
