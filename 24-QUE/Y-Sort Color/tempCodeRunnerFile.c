  int n; 
  int arr[n]; 

  printf("enter the size of array"); 
  scanf("%d",&n);  


  for(int i =0 ; i<n;i++){
    printf("enter the elements"); 
    scanf("%d", &arr[i]);
  } 

    //sort
  for(int turn=0;turn<n-1;turn++){
    for(int j=j+1;j<n-1;j++){
        if(arr[j] > arr[j+1]){
                // swap 
                int temp = arr[j]; 
                arr[j] = arr[j+1]; 
                arr[j+1] = temp;
            }
        }
    } 

    for(int i=0;i<n-1;i++){
        printf("%d",arr[i]);
    }  

    return 0; 