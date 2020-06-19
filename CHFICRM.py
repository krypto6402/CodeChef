# cook your dish here

# Python program to check whether X can  
# give change to every person in the Queue 
  
# Function to check if every person  
# will get the change from X 
def isChangeable(notes, n): 
      
    # To count the 5$ and 10& notes 
    fiveCount = 0
    tenCount = 0
      
    # Serve the customer in order 
    for i in range(n): 
          
        # Increase the number of 5$ note by one 
        if (notes[i] == 5): 
            fiveCount += 1
        elif(notes[i] == 10): 
              
            # decrease the number of note 5$  
            # and increase 10$ note by one 
            if (fiveCount > 0): 
                fiveCount -= 1
                tenCount += 1
            else: 
                return 0
        else: 
              
            # decrease 5$ and 10$ note by one 
            if ( tenCount > 0): 
                tenCount -= 1
                  
            # decrease 5$ note by three 
            elif (fiveCount >= 2): 
                fiveCount -= 2
            else: 
                return 0
    return 1
# Driver Code 

# queue of customers with available notes. 
for _ in range(int(input())):
    
    n = int(input()) 
    a=[int(a) for a in input().split()]
    
    # Calling function 
    if (isChangeable(a, n)): 
     print("YES") 
    else: 
     print("NO") 
    
    # This code is contributed by PrinciRaj1992
    
    
    
    
    
#   SELF (WRONG ANSWER)
'''
t=int(input())
for ti in range(t):
     n=int(input())
     a=list(map(int,input().split()))
     earnedmoney=0
     check=1
     for i in range(len(a)):
          if(a[i]==5):
               earnedmoney+=5
               continue
          returningmoney=a[i]-5
          if(returningmoney > earnedmoney):
               flag=0
               break
          else:
               earnedmoney = earnedmoney - returningmoney + 5
     if(check==0):
          print("NO")
     elif(check==1):
          print("YES")
'''
