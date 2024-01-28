
#include<stdio.h>
#include<conio.h> 

int main(){
    int n,temp,i,j,turn,k, gcd;  
  int arr[20]; 
  int s , l;
    
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


    printf("sorted array");
    for( i=0;i<n-1;i++){
        printf("%d\t",arr[i]);
    }  

    s = arr[0]; 
    l = arr[n-1];  

    printf("smallest number %d\n  largest number %d", s,l);
     
    // Gcd 
    for(k=1; k<=s && k<=l ;k++){
        if(s%k ==0 && l%k ==0){
            gcd = k;
        }
    } 
    printf("GCD is %d\n ",gcd);

    return 0 ;
}