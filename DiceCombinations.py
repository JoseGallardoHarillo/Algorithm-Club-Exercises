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

#dp[n]= dp[n−1] + dp[n−2] + dp[n−3] ... + dp[n - 6]

def diceCombinations(n, mem):
    #dice = [1,2,3,4,5,6] = Actions

    MOD = 10**9 + 7  # constraint module

    if(n == 0): return 1 #base case
    elif(n < 0): return 0 #constraint
    elif(n in mem): return mem[n]
    else:
        counter = 0  
        counter += (diceCombinations(n - 1, mem) + diceCombinations(n - 2, mem) + diceCombinations(n - 3, mem) + diceCombinations(n - 4, mem) + diceCombinations(n - 5, mem) + diceCombinations(n - 6, mem)) % MOD
        mem[n] = counter
    return counter

def main():
    #mem.clear
    mem = {} #Used to memorise the recursivity steps
    n = int(input())
    print(diceCombinations(n, mem))

main()