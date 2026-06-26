class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cost=prices[0]
        max_p=0

        for p in prices:
            min_cost=min(min_cost, p)
            max_p= max(max_p, p-min_cost)

        return max_p
        