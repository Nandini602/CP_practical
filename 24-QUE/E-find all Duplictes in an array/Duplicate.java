
import java.util.*;
public class Duplicate{

    public static void duplicates(int arr[]){
                
     for(int i =0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
              
                if((arr[i] == arr[j])){ 
                    System.out.println(arr[i]) ; 
                } 
                
            }

         }  
         
    }

    public static void main(String args[]){

        int arr[] = {4,3,2,7,8,2,3,1};
        duplicates(arr); 

    }
}