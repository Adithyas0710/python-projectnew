#include <stdio.h>
#include <string.h>
int main()
{ 
  char str1[30],str2[30];
  printf("Enter the first string:");
  scanf("%[^\n]",str1);
  printf("Enter the second string:");
  scanf("%s",str2);
  if(strcmp(str1,str2)==0)
    {
      printf("The strings are equal.\n");
    }
  else
    {
      printf("The strings are not equal.\n");
    }
  return 0;
 }
