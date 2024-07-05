class Solution:
    def maximumWealth(self, accounts) -> int:
        max_wealth = 0
        for row in accounts: 
            wealth = sum(row)
            max_wealth = max(wealth, max_wealth)
        return max_wealth
