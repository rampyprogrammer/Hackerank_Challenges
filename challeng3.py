def breakingRecords(scores):
    # Write your code here
    
    #intialize how many times the minimum and max score is broken
    min_records_broken=0
    max_records_broken=0
    
    # Initialize variables to keep track of the best and worst records
    min_score = scores[0]
    max_score = scores[0]
    
     # Iterate through the scores starting from the second game
    for score in scores[1:]:
        # Check if a new minimum record is achieved
        if score < min_score:
            min_score = score
            min_records_broken += 1
        # Check if a new maximum record is achieved
        elif score > max_score:
            max_score = score
            max_records_broken += 1

    return [max_records_broken, min_records_broken]
    
    

if __name__ == '__main__':
    n=int(input().strip())
    scores=[int(input()) for x in range(n)]
    res=breakingRecords(scores)
    print(res)