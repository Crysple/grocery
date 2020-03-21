class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profits = 0, lowest = INT_MAX;
        for (int price: prices){
            if (lowest > price) lowest = price;
            max_profits = max(price - lowest, max_profits);
        }
        return max_profits;
    }
};
