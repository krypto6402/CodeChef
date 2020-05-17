 #include<stdio.h>
 #include<math.h>
 int main()
{
   int t;
   scanf("%d",&t);
   while(t--)
   {
       long int n,a,b,c,d,p,q,y,walk,tra,i,tm;
       scanf("%ld%ld%ld%ld%ld%ld%ld%ld",&n,&a,&b,&c,&d,&p,&q,&y);
       int arr[n];
       for(i=1;i<=n;i++)
           scanf("%d",&arr[i]);
       walk=abs(arr[b]-arr[a])*p;
       tm=abs(arr[c]-arr[a])*p;
       if(tm<=y)
       {
        tra=y+(abs(arr[d]-arr[c])*q)+(abs(arr[d]-arr[b])*p);
           if(tra<walk)
            printf("%ld\n",tra);
           else
            printf("%ld\n",walk);
       }
       else
        printf("%ld\n",walk);
   }
	return 0;
}


