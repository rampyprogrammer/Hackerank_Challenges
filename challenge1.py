import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    # Create a dictionary to store the count of each sock color
    sock_count = {}
    
    # Initialize a variable to store the count of matching pairs
    pairs_count = 0
    
    # Iterate through the array of socks
    for sock in ar:
        # Check if the sock color is already in the dictionary
        if sock in sock_count:
            # If yes, increment the count by 1
            sock_count[sock] += 1
        else:
            # If not, add the sock color to the dictionary with a count of 1
            sock_count[sock] = 1
    print(sock_count)
    
    # Iterate through the dictionary to count the pairs
    for count in sock_count.values():
        pairs_count += count // 2  # Count the number of pairs for each color
    
    return pairs_count

if __name__ == '__main__':
    n=7
    ar=[10,10,20,10,20,30,30,20]
    result = sockMerchant(n, ar)
    print(result)
