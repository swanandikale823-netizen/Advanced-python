import random

# Reward values for cities
reward = [random.randint(10, 100) for i in range(8)]
print("City Rewards:", reward)


dp = [0] * len(reward)
dp[0] = reward[0]
dp[1] = max(reward[0], reward[1])

for i in range(2, len(reward)):
    dp[i] = max(dp[i-1], dp[i-2] + reward[i])

print("Maximum Reward:", dp[-1])



def rob(i):
    if i >= len(reward):
        return 0
    return max(reward[i] + rob(i+2), rob(i+1))

print("Recursive Reward:", rob(0))		
												
												
