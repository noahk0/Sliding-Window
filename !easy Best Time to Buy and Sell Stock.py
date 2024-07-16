def maxProfit(self, prices: List[int]) -> int:
    profit, dip = 0, prices[0]

    for price in prices:
        if price < dip:
            dip = price
        elif profit  + dip < price:
            profit = price - dip

    return profit
