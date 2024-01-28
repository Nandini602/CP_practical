
import java.util.*; 
public class Matrix{  

    public static boolean searchelements( int matrix[][] , int key){
         
         int row =0;
         int col=matrix[0].length-1; 
         while(row<matrix.length && col>=0){
            if(matrix[row][col] == key){
                return true;
            }
         
         else if(key < matrix[row][col]){
            col --;
         } 
         else{
            row++;
         }  

         } 

         return false;

    }


   
    public static void main(String args[]){ 

        Scanner sc = new Scanner(System.in); 
        System.out.println("enter the value of row and col");
        int row = sc.nextInt();
        int col = sc.nextInt(); 

        int matrix[][] = new int[row][col]; 

        for(int i=0;i<row;i++){
            for(int j= 0;j<col;j++){ 
                matrix[i][j] = sc.nextInt();
             }
        } 

        //print all elements 
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                System.out.print(matrix[i][j] + " ");
            } 
            System.out.println();
        } 

        int target = sc.nextInt();
        System.out.println(searchelements(matrix,target));


    }
}