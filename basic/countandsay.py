def countnndSay(n): 
      
    # Base cases 
    if (n == 1): 
        return "1"
    if (n == 2): 
        return "11"
  
    s = "11" 
    for i in range(3, n + 1): 
          

        s += '$'
        l = len(s) 
        
        cnt = 1 # Initialize count  
                # of matching chars 
        tmp = "" # Initialize i'th  
                 # term in series 
  
        # Process previous term to 
        # find the next term 
        for j in range(1 , l): 
              
            # If current character 
            # does't match 
            
            if (s[j] != s[j - 1]): 
                tmp += str(cnt + 0) 
                tmp += s[j - 1] 
                cnt = 1
            
            else: 
                cnt += 1
  
        s = tmp 
    return s; 
  
# Driver Code 
N = 5

print("The Sequence is")

for i in range(1,N):
   print(countnndSay(i))

print("\nAnswer to the Question is")

print(countnndSay(N))

