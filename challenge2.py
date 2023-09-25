#sum of arrays 
def sumOfArr(ar):
    #intialze variable to store the sum of value
    sum=0
    for val in ar:
        sum+=val

    return sum

if __name__ == '__main__':
    n=int(input("enter the no of values u want to  add to array : "))
    ar=[int(input("enter val : ")) for x in range(n)]
    res=sumOfArr(ar)
    print(res)