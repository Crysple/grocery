class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        if (prices.size() < 2) return 0;
        if (k >= prices.size()/2){
            int max_profits = 0;
            for (size_t i = 1; i < prices.size(); ++i){
                max_profits += max(0, prices[i] - prices[i-1]);
            }
            return max_profits;
        }
        vector<int> profits(prices.size(), 0);
        int local_max, max_profits = 0, tmp = 0;
        while (k--){
            local_max = -prices[0];
            for (size_t i = 1; i < prices.size(); ++i){
                tmp = max(local_max, profits[i]-prices[i]);
                profits[i] = max(profits[i-1], local_max+prices[i]);
                local_max = tmp;
                max_profits = max(max_profits, profits[i]);
            }
        }
        return max_profits;
    }
};
