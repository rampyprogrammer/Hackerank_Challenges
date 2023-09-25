#reducing the string 
#example i/p : s="aaabbcc"
def ReduceString(s):
    stack=[]
     
    for char in s:
        if stack and stack[0]==char:
           stack.remove(char)
        else:
            stack.append(char)
    
    if not stack:
        print("empty string")

    else:
        print("".join(stack))
    
ReduceString("aaabcccddd")
           