import java.util.Scanner;

public class Sequence {
    public static boolean isSubsequence(String s, String t) {
        int n = s.length();
        int m = t.length();
        int i = 0;
        int j = 0;
        while (i < n && j < m) {
            if (s.charAt(i) != t.charAt(j)) {
                j++;
            } else {
                i++;
                j++;
            } 
            if (i == n) {
            return true;
            } 

            return true;

        }
        
        return false;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        String t = scanner.nextLine();
        System.out.println(isSubsequence(s, t));
    }
}
