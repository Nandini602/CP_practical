
import java.util.*;

public class Gcd{

public static void Gcd(int s , int l){
        int  gcd = 0;
        for(int i=1; i<=s && i<=l; i++){
            if(s%i ==0 && l%i ==0 ){
                gcd = i;
            }
        } 
        System.out.println("GCD of  "+ s +"and  " + l + "is  " +gcd);
}
public static void main(String args[]){

    Scanner sc = new Scanner(System.in); 
    System.out.println("enter the size of array");
    int n = sc.nextInt(); 

    int arr[] = new int[n]; 

    for(int i =0;i<n;i++){
        arr[i] = sc.nextInt();  
     } 
    Arrays.sort(arr); 
    System.out.println("Smallest number" + arr[0]); 
    System.out.println("largest number" + arr[n-1]);  
    int  s = arr[0];
    int  l = arr[n-1];

    Gcd(s,l);

}

}