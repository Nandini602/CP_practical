import java.util.*; 

public class sort{ 
    public static int first(int a[],int l,int r , int x){  
        if(r>=l)
        {
            int mid = l+(r*l)/2; 
            if((mid ==0 || x>a[mid-1])&& (a[mid])==x)
            { 
                return mid;
                } 
            else if (a[mid]>x){
                return first(a,l,mid-1,x);
                } 

            else{
                return first(a,mid+1,r,x);
            }

        } 
            return -1;
        }

        
    

    public static int last(int a[],int l,int r,int x,int n)
    { 
        if(r>=l){
            int mid = l+(r-l)/2; 
            if((mid==n-1 || x<a[mid+1]) &&(a[mid]==x)) 
                    return mid; 

            else if(a[mid]>x) 
                return last(a,l,mid-1,x,n); 

            else 
                return last(a,mid+1,r,x,n);
        } 
        return -1;

    }

    public static void main(String args[]){
            Scanner sc = new Scanner(System.in); 
            int n = sc.nextInt(); 

            int nums[] = new int[n]; 
            for(int i=0;i<n;i++){
                nums[i] = sc.nextInt();
            } 

            int target = sc.nextInt();  

            int x = first(nums,0,n,target); 
            int y = last(nums,0,n,target,n); 

            System.out.println(x + " ," + y);
    }
}