
import java.util.*; 
public class colorsort{ 

    public static void sort(int arr[]){  
        for(int turn=0; turn<arr.length-1; turn++){
            for(int j=0; j<arr.length-1-turn; j++){ 
            if(arr[j] > arr[j+1]){

                // swap 

                int temp = arr[j]; 
                arr[j] = arr[j+1]; 
                arr[j+1] = temp;
            }
        } 
        }
    }  



    

    public static void main(String args[]){ 
        
        Scanner sc = new Scanner(System.in); 
        System.out.println("enter the size of array");
        int  n = sc.nextInt(); 
        int arr[] = new int[n]; 


        System.out.println("enter array"+n +" elements");

        for(int i=0;i<arr.length;i++){
             arr[i] = sc.nextInt(); 
        } 

         sort(arr);   
        
        for(int i=0;i<arr.length;i++){
             System.out.print(arr[i] + " ");
        } 
        
    }
}