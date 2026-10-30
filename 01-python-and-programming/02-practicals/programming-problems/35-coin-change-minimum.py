"""For positive integer denominations, find minimum coins for a nonnegative amount, or−1."""
def solve(coins,amount):
    if amount<0 or any(c<=0 for c in coins):raise ValueError('domain')
    dp=[0]+[amount+1]*amount
    for total in range(1,amount+1):
        for coin in coins:
            if coin<=total:dp[total]=min(dp[total],1+dp[total-coin])
    return dp[amount] if dp[amount]<=amount else -1
assert solve([1,3,4],6)==2 and solve([2],3)==-1 and solve([],0)==0
