#include<stdio.h>
#include<string.h>
const int max=1e5;

int main(void)
{
    int t;
    
    scanf("%d",&t);
    while(t--)
    {
        char s[3*max];
        scanf("%s", s);
        int c1=0;
        for(int i=0;i<strlen(s);++i)
        {
            if(s[i]=='x' && s[i+1]=='y') 
            {c1++;i++;}
            else if(s[i]=='y' && s[i+1]=='x')
            {c1++;i++;}
        }
          printf("%d\n",c1); 
    }

	return 0;
}
