#include<stdio.h>
#include<conio.h> 
int main()
{
     
  int n,temp,i,j,turn;  
  int arr[20];
    
  printf("enter the size of array"); 
  scanf("%d",&n);  

  for( i=0; i<n;i++){
    printf("enter the elements");
    scanf("%d", &arr[i]);
  } 

    //sort 

    for(turn=0; turn<n ;turn ++)
    for(j = 0 ; j<n ;j++){
        if(arr[j]> arr[j+1]){
            temp = arr[j]; 
            arr[j] = arr[j+1]; 
            arr[j+1] = temp;
        }
    } 



    for( i=0;i<n-1;i++){
        printf("%d\t",arr[i]);
    }  

    return 0; 


}