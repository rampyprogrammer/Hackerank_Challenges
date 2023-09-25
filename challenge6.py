#compare the triplets
def Triplerts(a,b):
    n=len(a)

    #intializing bob and Alice score from zero
    Bob_score=0
    Alice_score=0

    for  i in range(n):
        if a[i] > b[i]:
            Bob_score += 1
        elif a[i] < b[i]:
            Alice_score += 1

    return Alice_score, Bob_score

a=[1,2,3]
b=[3,2,1]
res=Triplerts(a,b)

