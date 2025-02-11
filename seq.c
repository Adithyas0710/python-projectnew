#include <stdio.h>
int main()
{
int n,i,key,flag=0,position=0;
printf("Enter the array size:");
scanf("%d",&n);
printf("Enter the elements:");
int a[n];
for(i=0;i<n;i++)
 {
  scanf("%d",&a[i]);
  }
 printf("enter the value to search:");
 scanf("%d",&key);
for(i=0;i<n;i++)
 { 
  if(key==a[i])
  {
   flag=1;
   position=i;
   break;
   }
  }
 if(flag==0)
  {
   printf("The element is not found!");
  }
 else
 {
  printf("The element %d is at %d ",key,position);
  }
 return 0;
 }
 

