#include <stdio.h>
int main() 
{
      long int n,h,y2;
      int i,j,t,y1,l,x,y,barr=0;
      scanf("%d",&t);
      for(int i=0;i<t;i++)
      {   barr=0;
          scanf("%ld %ld %d %ld %d",&n,&h,&y1,&y2,&l); 

          for(j=0;j<n;++j)
          {
               scanf("%d %d",&x,&y);
               if(l!=0)
               {      
                if(x==1)
                {
                    if((h-y1)>y)
			l--;
			barr++;
				
                }
                else if(x==2)
                {  
                    if(y2<y)
			l--;
			barr++;
                }
               }
               else
                    continue;
          }
          if(l==0)
		    printf("%d\n",barr-1);
		else
		    printf("%d\n",barr);
     } 
      return 0;
}

