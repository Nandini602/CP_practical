
import java.util.*;
public class Prefix{
     
        
        public static boolean Searching(int matrix[][], int  target){
            int r= 0 ;
            int c = matrix[0].length-1;  

            while(r<matrix.length && c>=0){
                if(matrix[r][c] == target){
                    return true;
                } 
                else if(target < matrix[r][c]){
                    c--;
                } 
                else{
                    c++;
                } 
                
            }  
            return false;
        }

        public static void main(String args[]){
        Scanner sc = new Scanner(System.in); 
        // enter the size
         
        int row = sc.nextInt(); 
        int col = sc.nextInt();  
         int matrix[][] = new int[row][col];  

        
        for(int i=0;i<row;i++){
            for(int j=0; j<col;j++){
                //System.out.println("row  ["+ i +"];  column " + j+ " ;"); 
                matrix[i][j] = sc.nextInt();
            }
        } 
        
        for(int i=0;i<row;i++){
            for(int j=0;j<n;j++){
                System.out.println(matrix[i][j]+ " ");
                System.out.println();
            }
        }
        int target = sc.nextInt(); 
        Searching(matrix,target);


        
    }
}