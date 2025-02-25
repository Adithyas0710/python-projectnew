#include <stdio.h>
int main()
{  
   char str[40],temp;
   int i,j,len;
   printf("Enter the string:");
   scanf("%[^\n]",str);
   for(len=0;str[len]!='\0';len++);
   i=len-1;
   {
   for(j=0;j<len/2;j++,i--)
     {
        temp=str[i];
        str[i]=str[j];
        str[j]=temp;
    }
    }
   printf("\n Reversed string:%s",str);
   return 0;
 } 
   
