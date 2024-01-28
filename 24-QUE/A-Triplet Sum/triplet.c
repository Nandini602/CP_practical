
#include<stdio.h>
int main(){
    int i,j, max=0; 
    scanf("%d%d",&i,&j); 
    for(int n=i;n<=j;n++){
        int m=n;
        int count =1;
        while(m!=1){
            if(m%2 ==0)
                m/=0;
            else 
                m = m*3+1; 
            count++;
        } 

        if (count>max)
            max = count;
        
     } 

    prinf("%d%d%d",i,j,max); 
    return 0;
}