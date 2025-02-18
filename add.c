#include <stdio.h>
int main()
{
   int i,j,rows,cols,row1,col1,A[10][10],B[10][10],sum[10][10];
   printf("Enter the size of rows and columns of first matrix:");
   scanf("%d%d",&rows,&cols);
   printf("Enter the size of rows and columns of second matrix:");
   scanf("%d%d",&row1,&col1);
   if (rows!=row1 && cols!=col1)
    {
     printf("Matrix addition is not possible!");
     return 0;
    }
  else
   {
   printf("Enter the elements of the first matrix:\n");
   for (i=0;i<rows;i++)
      {
       for(j=0;j<cols;j++)
         {
          printf("Elements[i][j]:");
          scanf("%d",&A[i][j]);
         }
      }  
   printf("Enter the elements of the second matrix:\n");
   for (i=0;i<row1;i++)
       {
        for(j=0;j<col1;j++)
         {
          printf("Elements[i][j]:");
          scanf("%d",&B[i][j]);
         }
       }
   for(i=0;i<rows;i++)
       {
       for(j=0;j<cols;j++)
         {
            sum[i][j]=A[i][j]+B[i][j];
           }
          
        }
      }
   printf("\n Resultant sum matrix:\n");
    for(i=0;i<rows;i++)
      { 
        for(j=0;j<cols;j++)
         {
          printf(" %d",sum[i][j]);
         }
        printf("\n");
      }
        return 0;
}   
           

