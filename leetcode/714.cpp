class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        if (!prices.size()) return 0;
        int low = prices[0], prehigh = prices[0], profits = 0;
        for (int i = 1; i < prices.size(); ++i){
            if (prices[i] < prehigh - fee){
                if (prehigh - low - fee > 0)
                    profits += prehigh - low - fee;
                low = prehigh = prices[i];
            }
            else if (low > prices[i]){
                low = prehigh = prices[i];
            }
            else if (prehigh < prices[i]){
                prehigh = prices[i];
            }
        }
        if (fee < prehigh - low){
            profits += prehigh - low - fee;
        }
        return profits;
    }
};
