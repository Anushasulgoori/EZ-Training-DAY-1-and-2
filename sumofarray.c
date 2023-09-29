//sum of array elements
#include<stdio.h>
int main()
{
  int i,n;
    printf("Enter arry size: ");
    scanf("%d",&n);
    int arr[n];
    int s=0;
    printf("Enter elements: ");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
        s+=arr[i];
    }
    printf("%d",s);
}

