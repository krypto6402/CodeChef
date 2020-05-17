#include<stdio.h>
#include<math.h>
int main()
{
     float t,f,dtb,ta,bs;
     float tt,bt;
     scanf("%f",&t);
     for(int i=0;i<t;i++)
     {
          scanf("%f %f %f %f",&f,&dtb,&ta,&bs);
          tt=sqrt(2*(f+dtb)/ta);
          bt=(f/bs);
          if(tt<=bt)
          printf("Tiger");
          else
          printf("Bolt");
          printf("\n");
     }
     return 0;
}