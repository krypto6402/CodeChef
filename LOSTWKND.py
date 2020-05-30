#include <stdio.h>
int main(void)
{
     int t;
     scanf("%d",&t);
     int i,a[5],p,sum;
     while(t--)
     {
          for(i=0;i<5;i++)
          scanf("%d",&a[i]);
          scanf("%d",&p);
          sum=0;
          for(i=0;i<5;i++)
          sum=sum+(p*a[i]);
          
          if (sum<=120)
          printf("No\n");
          else
          printf("Yes\n");
          
     }
	return 0;
}
