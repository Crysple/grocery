class Solution {
private:
    vector<int> forwardMaxProfit(vector<int>& prices) {
        vector<int> fprofits {0};
        int max_profits = 0, lowest = INT_MAX;
        for (int price: prices){
            if (lowest > price) lowest = price;
            max_profits = max(price - lowest, max_profits);
            fprofits.push_back(max_profits);
        }
        return fprofits;
    }
    vector<int> backwardMaxProfit(vector<int>& prices) {
        vector<int> bprofits {0};
        int max_profits = 0, highest = 0, price = 0;
        for (int i = int(prices.size()-1); i >= 0; --i){
            price = prices[i];
            if (highest < price) highest = price;
            max_profits = max(highest - price, max_profits);
            bprofits.push_back(max_profits);
        }
        return bprofits;
    }
public:
    int maxProfit(vector<int>& prices) {
        auto fprofits = forwardMaxProfit(prices);
        auto bprofits = backwardMaxProfit(prices);
        int max_profit = 0, N = fprofits.size();
        for (int i = 0; i < N; ++i){
            max_profit = max(max_profit, fprofits[i] + bprofits[N-i-1]);
        }
        return max_profit;
    }
};
