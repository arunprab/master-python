#Validate result of simple string compression

# aaaabbbcdaaa and a4b3cda3 - true
# aaaabbbcdaaa and a5b3cda3 - false

# Write a function that validates that two strings like this are equivalent.

# def function(text_a, text_b):
#   return true/false



# Coding for Comapring two Strings (Plain & Encrypted)


# aabb and a4b3cda3
# i, count, tmp

# aabb.....d[f]..."
input_s = "aabb"
second_s = "a2b2"

l = len(input_s) #Length of the 1st String
input_s += '$'

tmp = ""         #Temp Empty String
count = 1
    
for i in range (0, l):
        
    if input_s[i] != input_s[i+1]: # i=20 -> true, count=2, tmp=a2
        # tmp += X -> a
        # tmp += Y -> 2
        tmp += input_s[i]   # ? d
        if (count>1):
            tmp += str(count)     # ? 21
        count = 1
        # tmp = a2
    else:
        count += 1
        #tmp += input_s[i] + count #Need to check & modify
            
            
    result = tmp
    print(result)
    
if (result == second_s):
    print("True")
else:
    print("False")


