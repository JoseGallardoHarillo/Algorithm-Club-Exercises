'''
A - Dice Combinations

Your task is to count the number of ways to construct sum n by throwing a dice one or more times. 
Each throw produces an outcome between 1 and 6.

For example, if n=3, there are 4 ways:

* 1 + 1 + 1
* 1 + 2
* 2 + 1
* 3

-----Input-----
The only input line has an integer  n.

-----Output-----
Print the number of ways modulo 10^9 + 7.

-----Constraints-----
1 ≤ n ≤ 10^6

-----Example-----
input = 3
output = 4
'''

def diceCombinations(n):
    dice = [1,2,3,4,5,6]
    counter = 0

    for i in range(0,len(dice) - 1):
        for j in range(0,len(dice) - 1):
            if(i + j == n):
                counter += 1
    
    return counter

n = int(input("Introduce el valor de n: "))

print(diceCombinations(n))