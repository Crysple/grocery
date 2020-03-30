class Solution {
private:
    int get_max_profit_from(int from, const vector<int>& prices, vector<int>& max_profit_from) {
        if (from >= prices.size()) return 0;
        if (max_profit_from[from] != -1) return max_profit_from[from];
        int cur_profit = get_max_profit_from(from + 1, prices, max_profit_from);
        for (int i = from + 1; i < prices.size(); ++i){
            if (prices[i] < prices[from]) break;
            cur_profit = max(cur_profit, prices[i] - prices[from] + get_max_profit_from(i + 2, prices, max_profit_from));
        }
        max_profit_from[from] = cur_profit;
        return cur_profit;
    }
public:
    int maxProfit(vector<int>& prices) {
        auto max_profit_from = vector<int>(prices.size(), -1);
        return get_max_profit_from(0, prices, max_profit_from);
    }
};
