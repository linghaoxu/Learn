#include<stdio.h>
void main()
{int i, t, a[5];
 printf("Input 5 integers:\n");
 for(i=0; i<5; i++)
  scanf("%d",&a[i]);
 t=a[0];//Line 7
 for(i=1;i<5;i++)//Line 8
  a[i-1]=a[i];//Line 9
 a[4]= t;//Line 10
 printf("After rotation:\n");
 for(i=0;i<5;i++)
  printf("%5d",a[i]);
 printf("\n");
}
