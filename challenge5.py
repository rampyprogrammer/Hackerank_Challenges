def Pattern(n):
    for  i in range(n):
        for j in range(n):
            if i+j >= n-1:
                print("#",end="")
            else:
                print(" ",end="")
        print()
Pattern(int(input("enter num : ")))

